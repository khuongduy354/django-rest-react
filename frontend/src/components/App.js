import React, { Component } from "react";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Link,
  Redirect,
  Route,
  Switch,
} from "react-router-dom";
// components
import Homepage from "./Homepage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoompage";
import Room from "./Room";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      roomCode: null,
    };
    this.clearRoomCode = this.clearRoomCode.bind(this);
  }

  componentDidMount() {
    fetch("/api/user-in-room")
      .then((res) => res.json())
      .then((data) =>
        data.roomCode
          ? this.setState({
              roomCode: data.roomCode,
            })
          : this.setState({
              roomCode: null,
            })
      );
  }

  clearRoomCode() {
    this.setState({
      roomCode: null,
    });
  }
  render() {
    return (
      <Router>
        <Switch>
          <Route
            exact
            path="/"
            render={() => {
              return this.state.roomCode ? (
                <Redirect to={`/room/${this.state.roomCode}`} />
              ) : (
                <Homepage />
              );
            }}
          />
          <Route path="/join" component={RoomJoinPage} />
          <Route path="/create" component={CreateRoomPage} />
          <Route
            path="/room/:roomCode"
            render={(props) => {
              return <Room {...props} leaveRoomCallBack={this.clearRoomCode} />;
            }}
          />
        </Switch>
      </Router>
    );
  }
}

const divApp = document.getElementById("app");
render(<App name="Duy" />, divApp);
