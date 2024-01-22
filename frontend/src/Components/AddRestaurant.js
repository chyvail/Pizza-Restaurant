import React from "react";
import { useState } from "react";

export default function AddRestaurant() {
  const [formData, setFormData] = useState({
    name: "",
    address: "",
  });

  const handleButtonClick = () => {
    const modal = new window.bootstrap.Modal(
      document.getElementById("myModal")
    );
    modal.show();
  };

  const handleOnChange = (e) => {
    const key = e.target.id;
    setFormData({ ...formData, [key]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/restaurants", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((res) => {
        res.json();
        alert("Data has been added");
      })
      .then((data) => console.log(data));
    setFormData({
      name: "",
      address: "",
    });
  };

  return (
    <>
      <div className="mt-3 text-center">
        <button
          type="button"
          className="btn btn-light"
          onClick={handleButtonClick}
        >
          Add New Restaurant
        </button>
      </div>

      {/* Bootstrap Modal */}
      <div
        className="modal fade"
        id="myModal"
        tabIndex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog modal-dialog-centered">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title form-font" id="exampleModalLabel ">
                Add A New Restaurant
              </h5>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div className="modal-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="col-form-label form-font">
                    Restaurant Name
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="name"
                    onChange={handleOnChange}
                    value={formData.name}
                  />
                </div>
                <div className="mb-3">
                  <label className="col-form-label form-font">
                    Restaurant Address
                  </label>
                  <textarea
                    className="form-control"
                    id="address"
                    onChange={handleOnChange}
                    value={formData.address}
                  ></textarea>
                </div>
                <div className="modal-footer">
                  <button
                    type="button"
                    className="btn btn-secondary"
                    data-bs-dismiss="modal"
                  >
                    Close
                  </button>
                  <button type="submit" class="btn btn-primary btn-color">
                    Submit Form
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
