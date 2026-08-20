export type Research = { id: string; status: string; created_at: string; updated_at: string };

export async function createResearch(title: string): Promise<Research> {
  const response = await fetch("/research", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ title }) });
  if (!response.ok) throw new Error(`request failed: ${response.status}`);
  return response.json();
}

export async function getResearch(id: string): Promise<Research> {
  const response = await fetch(`/research/${encodeURIComponent(id)}`, { cache: "no-store" });
  if (!response.ok) throw new Error(`request failed: ${response.status}`);
  return response.json();
}

export function researchEvents(id: string, onEvent: (event: MessageEvent) => void): () => void {
  const source = new EventSource(`/research/${encodeURIComponent(id)}/events`);
  source.addEventListener("public", onEvent);
  return () => source.close();
}
