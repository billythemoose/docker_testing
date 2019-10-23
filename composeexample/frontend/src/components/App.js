import React, { Component } from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import axios from 'axios';

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
      selectedFile: null
    };

    
  }

  onChangeHandler = event => {
    console.log(`File being added: ${event.target.files[0].name}`);
    this.setState({
      selectedFile: event.target.files[0],
      loaded: 0,
    });
  };

  clickButton = event => {
    console.log("Sending file to be processed...");
    const data = new FormData();
    data.append('file', this.state.selectedFile);

    try {
      axios.post("http://localhost:8000/upload", data, {

      }).then(res =>  {
        console.log(res.statusText)
      });
    }
    catch (error) {
      console.log(error);
    }
  };

  render() {
    return (
      <div>
        <div>
          <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
        </div>
        <div className="container">
          <div className="row">
            <div className="col-md-6">
              <form method="post" action="#" id="#">
                <div className="form-group files">
                  <label>Upload Your Transcript </label>
                  <input type="file" className="form-control" multiple="" name="file" onChange={this.onChangeHandler} />
                </div>
              </form>
            </div>
            </div>
        </div>
        <div className="row">
          <div className="col-md-6">
              <div>
                <button type="button" onClick={this.clickButton}>Submit</button>
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