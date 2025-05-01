<<<<<<< HEAD
import React from "react";

type RecipeDisplayProps = {
  recipe: string;
};

const RecipeDisplay: React.FC<RecipeDisplayProps> = ({ recipe }) => {
  return (
    <div>
      <h2>Suggested Recipe</h2>
      <pre style={{ whiteSpace: "pre-wrap" }}>{recipe}</pre>
    </div>
  );
};

export default RecipeDisplay;
export {}; // to satisfy TS isolatedModules
=======
export {}; // makes it a module even if there's no export yet
>>>>>>> 00c439d49f1c59a7fb5de37faff52ddda88078ab
