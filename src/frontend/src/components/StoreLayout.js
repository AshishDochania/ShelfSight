import React from 'react';
import { Link } from 'react-router-dom';

const StoreLayout = ({ shelves }) => (
  <div className="store-layout">
    {shelves.map(shelf => (
      <Link to={`/shelf/${shelf.id}`} key={shelf.id}>
        <div className={`shelf ${shelf.stockLevel}`}>
          Shelf {shelf.id}
        </div>
      </Link>
    ))}
  </div>
);

export default StoreLayout;