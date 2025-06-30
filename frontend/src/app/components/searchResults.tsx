// components/SearchResults.tsx
import React from 'react';
import { Document } from '../models/document';

export default function SearchResults({ results }: { readonly results: readonly Document[] }) {
  return (
    <div>
      {results && results.length > 0 ? (
        results.slice(0, 5).map((result, index) => (
          <div key={result.filename + index}>
            <h2 className="text-lg font-semibold">{result.filename}</h2>
            <div className="text-sm text-gray-500">Score: {result.score.toFixed(2)}</div>
            <div className="text-sm text-gray-500">Preview: {result.preview}</div>
            <hr className="my-4" />
          </div>
        ))
      ) : (
        <p>No results found yet.</p>
      )}
    </div>
  );
}
