# Creating 3-D scatterplots

# Load data
?iris
data(iris)
iris[1:5, ]

# Static 3D scatterplot
# Install and load the "scatterplot3d" package
install.packages("scatterplot3d")
require("scatterplot3d")

# Basic static 3D scatterplot
scatterplot3d(iris[1:3])

# Modified static 3D scatterplot
# Coloring, vertical lines
# and Regression Plane 
s3d <-scatterplot3d(iris[1:3],
                    pch = 16,
                    highlight.3d = TRUE,
                    type = "h",
                    main = "3D Scatterplot")
plane <- lm(iris$Petal.Length ~ iris$Sepal.Length + iris$Sepal.Width) 
s3d$plane3d(plane)

