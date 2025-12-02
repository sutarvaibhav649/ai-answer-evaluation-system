import mongoose from "mongoose";
import dotenv from "dotenv";
dotenv.config();

mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log("MongoDB Connection Successful!");
    process.exit(0);
  })
  .catch((err) => {
    console.error("MongoDB Connection Failed:", err);
    process.exit(1);
  });
