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
