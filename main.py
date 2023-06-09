
class MousePath:
    def __init__(self, ) -> None:
        self.matrix = []
        self.size = 0
        self.max_result = 0

    # Text-to-matrix translation function
    def init_matrix(self, filename: str):
        self.matrix = []
        text = None
        with open(filename) as f:
            text = f.readlines()
        
        for line in text:
            row = [int(num_str.strip()) for num_str in line.split(",")]
            self.matrix.append(row)
        self.size = len(self.matrix)

    def most_valuable_path(self, start_x, start_y):

        def dfs(matrix, current_x, current_y):
            field_value = matrix[current_x][current_y]
            matrix[current_x][current_y] = 0

            result = 0
            visited = 0


            # Down
            if 0 <= (current_x + 1) < self.size and 0 <= current_y < self.size and matrix[current_x + 1][current_y] > field_value:
                result = dfs(matrix, current_x + 1, current_y) + field_value
                self.max_result = max(result, self.max_result)
                visited = 1

            # Up
            if 0 <= (current_x - 1) < self.size and 0 <= current_y < self.size and matrix[current_x - 1][current_y] > field_value:
                result = dfs(matrix, current_x - 1, current_y) + field_value
                self.max_result = max(result, self.max_result)
                visited = 1

            # Right
            if 0 <= current_x < self.size and 0 <= (current_y + 1) < self.size and matrix[current_x][current_y + 1] > field_value:
                result = dfs(matrix, current_x, current_y + 1) + field_value
                self.max_result = max(result, self.max_result)
                visited = 1

            # Left
            if 0 <= current_x < self.size and 0 <= (current_y - 1) < self.size and matrix[current_x][current_y - 1] > field_value:
                result = dfs(matrix, current_x, current_y - 1) + field_value
                self.max_result = max(result, self.max_result)
                visited = 1

            if not visited:
                result = field_value

            matrix[current_x][current_y] = field_value

            return result
        
        dfs(self.matrix, start_x, start_y)

        return self.max_result


if __name__ == "__main__":
    mouse_path = MousePath()
    mouse_path.init_matrix("matrix.txt")

    print(mouse_path.most_valuable_path(0, 0))
    
    print(mouse_path.matrix)
    print(mouse_path.size)

# Matrix to tests:
# 1,2
# 5,4

