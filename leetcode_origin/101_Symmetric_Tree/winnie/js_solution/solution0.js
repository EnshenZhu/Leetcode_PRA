/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 const dfs=(nodeA,nodeB)=>{
    if ((nodeA==null) && (nodeB==null)){
        return true;
    }
    else if ((nodeA==null) || (nodeB==null)){
        return false;
    }
    else if (nodeA.val != nodeB.val){
        return false;
    }
    
    else{
        return dfs(nodeA.left,nodeB.right) && dfs(nodeA.right,nodeB.left);
    }
    
}

var isSymmetric = function(root) {
    if (root==null) return true;
    return dfs(root,root)
};

console.log(isSymmetric(root = [1,2,2,3,4,4,3]))
console.log(isSymmetric(root = [1,2,2,null,3,null,3]))