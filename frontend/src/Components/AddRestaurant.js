import React from "react";

export default function AddRestaurant() {
  const handleButtonClick = () => {
    const modal = new window.bootstrap.Modal(
      document.getElementById("myModal")
    );
    modal.show();
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
              <form>
                <div className="mb-3">
                  <label className="col-form-label form-font">
                    Restaurant Name
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="restaurant-name"
                  />
                </div>
                <div className="mb-3">
                  <label className="col-form-label form-font">
                    Restaurant Address
                  </label>
                  <textarea
                    className="form-control"
                    id="restaurant-address"
                  ></textarea>
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button type="button" class="btn btn-primary">
                Submit Form
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
