# 3-D scatterplot
require("rgl")
require("RColorBrewer")
plot3d(vocab$YEAR,  # x variable
       vocab$EDUCATION,   # y variable
       vocab$VOCABULARY,  # z variable
       xlab = "YEAR",
       ylab = "EDUCATION",
       zlab = "VOCABULARY",
       col = rainbow(1000),
       size = 8)