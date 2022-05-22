import axios from "axios";
const USER_BASE_URL = "http://localhost:3000/user";
const headers = {
  "Content-Type": "application/json",
  Authorization: "Token " + localStorage.getItem("token"),
};

class UserService {
  loginUser(credentials) {
    // fetch('url', {
    //   method : 'POST',
    //   headers: {
    //     "Content-Type": "application/json",
    //     Authorization: "Token " + localStorage.getItem("token"),
    //   }
    // })
    return axios.post(USER_BASE_URL + "/login", credentials);
  }
  // get user
  getUser() {
    console.log(headers);
    headers.Authorization = "Token " + localStorage.getItem("token");
    return axios.get(USER_BASE_URL, { headers: headers });
  }

  // post user
  postUser(users) {
    console.log(headers);
    return axios.post(USER_BASE_URL, users, { headers: headers });
  }

  // delete user
  deleteUser(id) {
    console.log(headers);
    return axios.delete(USER_BASE_URL + "/" + id, { headers: headers });
  }
}

export default new UserService();