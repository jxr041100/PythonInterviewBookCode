def maxPathSum(root: 'TreeNode') -> int:
    best_sum = -float('inf')                   # tracker for best sum
    def maxPath(v: 'vertex'):                  # define helper function
        nonlocal best_sum                      # reference our tracker
        if v is None:                          # base case
            return 0
        L = maxPath(v.left)                    # recurse on left child
        R = maxPath(v.right)                   # recurse on right child
        # 用子树总和更新跟踪器
        best_sum = max(best_sum, v.val+L+R)
        # 返回父子树的最佳分支
        return max(0, v.val+L, v.val+R)
    maxPath(root)                               # run recursive traversal
    return best_sum
