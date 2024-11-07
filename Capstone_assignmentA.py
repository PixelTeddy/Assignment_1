import matplotlib.pyplot as plt
import numpy as np

def draw_circle(ax, center, radius, color, fill=True, edgecolor=None, linewidth=1):
    circle = plt.Circle(center, radius, color=color, fill=fill, edgecolor=edgecolor, linewidth=linewidth)
    ax.add_patch(circle)

def draw_half_circle(ax, center, radius, color, angle, edgecolor=None, linewidth=1):
    half_circle = plt.Polygon([
        (center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta))
        for theta in np.linspace(angle, angle + np.pi, 50)
    ], color=color, edgecolor=edgecolor, linewidth=linewidth)
    ax.add_patch(half_circle)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')

body_color = "#D2691E"      
ear_color = "#8B4513"       
eye_color = "black"         
nose_color = "black"        
mouth_color = "black"       
inner_ear_color = "#DEB887" 

draw_circle(ax, (0, 0), 1, body_color)           

draw_circle(ax, (-0.7, 0.8), 0.3, ear_color)     
draw_circle(ax, (0.7, 0.8), 0.3, ear_color)      
draw_circle(ax, (-0.7, 0.8), 0.15, inner_ear_color) 
draw_circle(ax, (0.7, 0.8), 0.15, inner_ear_color)  

draw_circle(ax, (0, 0.4), 0.6, body_color)       
draw_circle(ax, (-0.25, 0.5), 0.1, eye_color)    
draw_circle(ax, (0.25, 0.5), 0.1, eye_color)     
draw_circle(ax, (0, 0.25), 0.1, nose_color)      

draw_half_circle(ax, (0, 0.1), 0.15, mouth_color, -np.pi / 2) 

plt.show()
