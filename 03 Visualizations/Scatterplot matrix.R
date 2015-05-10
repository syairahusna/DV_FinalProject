# Scatterplot matrix using "pairs"
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
      main = "Scatterplot Matrix for HUbway Data",
      diag.panel = panel.hist, 
      pch = 16, 
      col = "lightgray")
