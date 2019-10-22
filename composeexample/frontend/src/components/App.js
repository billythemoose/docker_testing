import React, { Component } from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";

/*
const App = () => (
  <div>
    <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
  </div>
);
*/


/*
const dataTable = (
  <div>
    <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
    <button className="btn btn-default">Testing Button</button>
  </div>
);
*/
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isAuthenticated: false
    };
  }

  render() {
    return (
      <div>
        <div>
          <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
        </div>
        <div class="container">
          <div class="row">
            <div class="col-md-6">
              <form method="post" action="#" id="#">
                <div class="form-group files">
                  <label>Upload Your Transcript </label>
                  <input type="file" class="form-control" multiple="" />
                </div>
              </form>
            </div>
            </div>
        </div>
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById("app")
);


/*
const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;
*/