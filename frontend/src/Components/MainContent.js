import React, { useEffect, useState } from "react";
import AddRestaurant from "./AddRestaurant";

export default function MainContent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/restaurants")
      .then((response) => response.json())
      .then((resdata) => setData(resdata));
  }, []);

  return (
    <div className="container-lgs mt-3">
      <div className="row g-2">
        <div className="text-center">
          <h5>Available Restaurants</h5>
        </div>
        {data.map((item) => (
          <div key={item.id} className="col-sm-6">
            <div className="card text-white bg-success">
              <div className="card-header">Restaurant Name</div>
              <div className="card-body">
                <h5 className="card-title">{item.name}</h5>
                <p className="card-text">
                  <i className="fa-solid fa-building svg-icon"></i>
                  {item.address}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <AddRestaurant />
    </div>
  );
}
