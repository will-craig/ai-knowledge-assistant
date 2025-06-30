// components/SearchBox.tsx
'use client';
import React, { useState } from 'react';

export default function SearchBox({ onResults }: { onResults: (data: any) => void }) {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    const res = await fetch('http://localhost:8000/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, top_k: 3 }),
    });

    const data = await res.json();
    onResults(data);
  };

  return (
    <div className="p-4 border rounded mt-4">
      <input
        type="text"
        placeholder="Ask something..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border px-2 py-1"
      />
      <button onClick={handleSearch} className="bg-green-500 text-white px-4 py-2 ml-2 rounded">
        Search
      </button>
    </div>
  );
}
