class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        [[1,1,1],  
         [1,1,0],  
         [1,0,1]]

        [[2,2,2],  
         [2,2,0],  
         [2,0,1]]

         Base Cases:
         No more adjacent pixels of original color to update
        When current pixel doesnt match original starting color
        When the current position is outside the image dimensions

        '''
        original_color = image[sr][sc]

        ROWS = len(image)
        COLS = len(image[0])

        def dfs(r, c, color):

            if (min(r, c) < 0 or r == ROWS or c == COLS):
                return
            if image[r][c] == color or image[r][c] != original_color:
                return 
            
            image[r][c] = color

            dfs(r + 1, c, color)
            dfs(r - 1, c, color)
            dfs(r, c + 1, color)
            dfs(r, c - 1, color)
        dfs(sr, sc, color)
        return image