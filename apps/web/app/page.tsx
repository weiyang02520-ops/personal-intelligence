"use client";

import { useEffect, useState } from "react";
import { createResearch, getResearch, researchEvents, type Research } from "../lib/pi-api";

export default function Home() {
  const [title, setTitle] = useState("");
  const [research, setResearch] = useState<Research | null>(null);
  const [events, setEvents] = useState<string[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit() {
    setBusy(true); setError(null); setEvents([]);
    try { setResearch(await createResearch(title)); } catch (err) { setError(String(err)); } finally { setBusy(false); }
  }

  useEffect(() => {
    if (!research) return;
    const close = researchEvents(research.id, (event) => setEvents((current) => [...current, event.data]));
    const timer = window.setInterval(() => getResearch(research.id).then(setResearch).catch(() => undefined), 500);
    return () => { close(); window.clearInterval(timer); };
  }, [research?.id]);

  return <main>
    <h1>Personal Intelligence</h1>
    <p>Physical architecture PoC: PI API lifecycle and public events.</p>
    <textarea value={title} onChange={(event) => setTitle(event.target.value)} placeholder="Research topic" />
    <button onClick={submit} disabled={busy}>{busy ? "Starting…" : "Start research"}</button>
    {error && <p role="alert">{error}</p>}
    {research && <section><h2>{research.status}</h2><p>{research.id}</p><pre>{events.join("\n") || "Waiting for public events…"}</pre></section>}
  </main>;
}
