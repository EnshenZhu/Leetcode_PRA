from collections import defaultdict


class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        result, adjacent_list = [], defaultdict(list)

        # build adjacency list

        for single_recipe, single_recipe_all_ingredient in zip(recipes, ingredients):
            for single_ingredient in single_recipe_all_ingredient:
                adjacent_list[single_recipe].append(single_ingredient)

        print(adjacent_list)

        supplies, recipes = set(supplies), set(recipes)

        # dfs function --> True means not possible, false means possible
        def dfs(node, seen, cseen):

            if not adjacent_list[node] and node not in supplies:
                return True

            seen.add(node)
            cseen.add(node)
            for neighbor in adjacent_list[node]:  # node --> bread, neighbor --> yeast and flour
                if neighbor in supplies:
                    continue

                if neighbor not in seen:
                    dfs(neighbor, seen, cseen)
                elif neighbor in cseen:
                    return True

            cseen.remove(node)
            return False

        # calling the dfs function
        for single_recipe in recipes:
            if recipes in supplies:
                result.append(single_recipe)
            else:
                seen, cseen = set(), set()
                if not dfs(single_recipe, seen, cseen):
                    result.append(single_recipe)
                    supplies.add(single_recipe)

        return result
