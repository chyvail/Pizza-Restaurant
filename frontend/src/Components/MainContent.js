import React, { useEffect, useState } from "react";
import AddRestaurant from "./AddRestaurant";

export default function MainContent() {
  const [data, setData] = useState([]);

  const handleDelete = (id) => {
    fetch(`https://pizza-restaurant-jl0u.onrender.com/restaurants/${id}`, {
      method: 'DELETE',
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); 
      })
      .then(() => {
        alert("Restaurant has been Deleted");
        const updatedData = data.filter(item => item.id !== id);
        setData(updatedData);
      })
      .catch(error => console.error('Error deleting restaurant:', error));
  };  

  useEffect(() => {
    fetch("https://pizza-restaurant-jl0u.onrender.com/restaurants")
      .then((response) => response.json())
      .then((resdata) => setData(resdata));
  }, []);

  return (
    <div className="container-lgs mt-3">
      <div className="row g-2">
        <div className="text-center">
          <h5>Available Restaurants 🍜</h5>
        </div>
        {data.map((item) => (
          <div key={item.id} className="col-sm-6">
            <div className="card text-white bg-success">
              <div className="card-header d-flex justify-content-between align-items-center">
                <div>Restaurant Name</div>
                <i
                  className="fa-solid fa-ellipsis-vertical dropdown-toggle custom-ellipsis"
                  data-bs-toggle="dropdown"
                ></i>
                <ul className="dropdown-menu">
                  <li>
                    <button
                      className="dropdown-item"
                      onClick={() => handleDelete(item.id)}
                    >
                      Delete
                    </button>
                  </li>
                </ul>
              </div>
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
