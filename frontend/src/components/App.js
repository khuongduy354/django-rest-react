import React,{Component} from "react";
import {render} from "react-dom";
import { BrowserRouter as Router, Link, Redirect,Route,Switch } from "react-router-dom";
// components
import Homepage from "./Homepage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoompage";


export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <Router>
                <Switch>    
                    <Route exact path='/'component={Homepage} /> 
                    <Route path='/join' component={RoomJoinPage} />
                    <Route path='/create' component={CreateRoomPage} />
                </Switch>
            </Router>

        );
    }
}

const divApp=document.getElementById("app")
render(<App name="Duy" />,divApp);