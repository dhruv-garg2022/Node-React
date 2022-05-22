const express = require("express");
const router = express.Router();
const UserService = require("../services/UserService")
const auth = require("./auth");

router.get("/",auth.required,async (req,res)=>{
    const userService = new UserService();
    const result = await userService.getUser()
    res.send(result)
})

router.post("/", async (req,res)=>{
    const userService = new UserService();
    const result = await userService.setUser(req.body)
    res.send("User Created")
})

router.post("/login", async (req,res)=>{
    
    const userService = new UserService();
    const result = await userService.loginUser(req.body.email, req.body.password);
    console.log(result)
    res.send(result)
})

router.delete("/:id", async(req,res)=>{
    const userService = new UserService();
    const result = await userService.removeUser(req.params.id)
    res.send(result)
})

module.exports = router;