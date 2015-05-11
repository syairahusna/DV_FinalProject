# Scatterplot matrix using "pairs" for Hubway_Stations
panel.hist <- function(x, ...)
{
  usr <- par("usr"); on.exit(par(usr))
  par(usr = c(usr[1:2], 0, 1.5) )
  h <- hist(x, plot = FALSE)
  breaks <- h$breaks; nB <- length(breaks)
  y <- h$counts; y <- y/max(y)
  rect(breaks[-nB], 0, breaks[-1], y,  ...)
 }

pairs(hws[c(2:6)], 
      panel = panel.smooth,  # Optional smoother
      main = "Scatterplot Matrix for Hubway Data",
      diag.panel = panel.hist, 
      pch = 16, 
      col = "lightgray")


# Creating scatterplot matrices

names(hws)

# Basic Scatterplot Matrix
pairs(~TERMINAL + STATION + MUNICIPAL + LAT + LNG,
      data = hws, 
      pch = 20,
      main = "Simple Scatterplot Matrix for Hubway Stations")

# Use "Pairs Plot" from "psych" package
install.packages("psych")
library("psych")
pairs.panels(hws[c(2, 4, 5, 6)], gap = 0)
