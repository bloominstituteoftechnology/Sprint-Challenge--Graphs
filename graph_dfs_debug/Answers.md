Describe the fixes you made to the Graph implementation here.

1. OnButton function was not being called correctly on "Random" button click.
    -Note: It could also be shortened into a one-liner by just adding window.location.reload

2. Graph width wasn't taking up enough space to display all output, changed canvas height in App.js to be window.innerWidth

3. Issues with graph not showing as the same color to connected nodes, changed the way vertexes was being called in drawVerts for app.js

4. In graph.js for dfs arrays were using unknown methods, the component was being called as a new class.