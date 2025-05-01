import React, { useState } from "react";
import "./App.css";
import ImageUpload from "./Components/ImageUpload";
import RecipeDisplay from "./Components/RecipeDisplay";

function App() {
  const [recipe, setRecipe] = useState<string>("");

  return (
    <div className="App">
      <h1>What's Cookin'? 🥕</h1>
      <ImageUpload onResult={(data) => setRecipe(data)} />
      {recipe && <RecipeDisplay recipe={recipe} />}
    </div>
  );
}

export default App;