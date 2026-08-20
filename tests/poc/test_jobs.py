from __future__ import annotations

import time

from apps.core.database import Database
from apps.core.jobs import JobService
from apps.core.models import JobRecord


def make_jobs(tmp_path, lease_seconds=2):
    db = Database(f"sqlite:///{tmp_path / 'jobs.sqlite'}")
    db.create_schema()
    return db, JobService(db, lease_seconds=lease_seconds)


def test_job_claim_retry_heartbeat_and_complete(tmp_path):
    db, jobs = make_jobs(tmp_path)
    job_id = jobs.enqueue("research-1")
    claimed = jobs.claim_next()
    assert claimed is not None and claimed.id == job_id
    assert claimed.status == "RUNNING"
    assert jobs.heartbeat(job_id) is True
    jobs.fail(job_id, "temporary upstream failure", retry=True)
    time.sleep(0.06)
    retried = jobs.claim_next()
    assert retried is not None and retried.attempts == 2
    jobs.complete(job_id)
    with db.session() as session:
        row = session.get(JobRecord, job_id)
        assert row.status == "COMPLETED"
        assert row.last_error == "temporary upstream failure"


def test_stale_worker_is_recovered_and_can_be_restarted(tmp_path):
    db, jobs = make_jobs(tmp_path, lease_seconds=0)
    job_id = jobs.enqueue("research-2")
    first = jobs.claim_next()
    assert first is not None
    time.sleep(0.01)
    assert jobs.recover_stale() == 1
    restarted = jobs.claim_next()
    assert restarted is not None and restarted.id == job_id and restarted.attempts == 2
    jobs.complete(job_id)


def test_run_once_retries_failed_worker_without_duplicate_claim(tmp_path):
    _, jobs = make_jobs(tmp_path)
    jobs.enqueue("research-3")
    calls = []

    def fail_once(job):
        calls.append(job.id)
        raise RuntimeError("worker stopped")

    assert jobs.run_once(fail_once) is True
    time.sleep(0.06)
    assert jobs.run_once(lambda job: calls.append(job.id)) is True
    assert len(calls) == 2 and calls[0] == calls[1]
