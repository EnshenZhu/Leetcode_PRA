/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
    const recipesMap = buildReceiptsMap(recipes, ingredients);
    return recipesMap;
};

const buildReceiptsMap = (recipes, ingredients) => {
    const recipesMap = {};

    for (let idx = 0; idx < recipes.length; idx++) {
        recipesMap[recipes[idx]]=[];
        for (let singleIngredient of ingredients[idx]){
            recipesMap[recipes[idx]].push(singleIngredient)
        }        
    }

    return recipesMap;
}

console.log(findAllRecipes(recipes = ["bread"], ingredients = [["yeast", "flour"]], supplies = ["yeast", "flour", "corn"]))
// console.log(buildReceiptsMap(["bread"], [["yeast", "flour"]]))