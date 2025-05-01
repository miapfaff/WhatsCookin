import React, { useState } from "react";
import axios from "axios";

const ImageUpload = ({ onResult }: { onResult: (data: string) => void }) => {
  const [image, setImage] = useState<File | null>(null);

  const handleUpload = async () => {
    if (!image) return;
    const formData = new FormData();
    formData.append("file", image);
    const response = await axios.post("http://localhost:8000/upload", formData);
    onResult(response.data.recipe);
  };

  return (
    <div>
      <input type="file" onChange={(e) => e.target.files && setImage(e.target.files[0])} />
      <button onClick={handleUpload}>Generate Recipes</button>
    </div>
  );
};

export default ImageUpload;
