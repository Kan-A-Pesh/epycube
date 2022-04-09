# Journal de changements

## Version 0.0.4

**Message**:\
`🏃‍♂️ added player controller`

**Description**:\
Ajout d'un contrôleur pour le joueur, il peut sauter, marcher et subir la gravité.

**Changements** (.py uniquement):

```diff
+ src/main.py
+ src/player.py
```

## Version 0.0.3

**Message**:\
`🎄 added chunks perlin noise generation`

**Description**:\
Ajout de tronçons (par defaut 16x16x16 cubes) et génération procédurale par bruit de Perlin.

**Changements** (.py uniquement):

```diff
+ src/chunk.py
- src/cube.py
+ src/noise.py
+ src/main.py
```

## Version 0.0.2

**Message**:\
`🧊 added a cube`

**Description**:\
Ajout d'un cube avec des faces.

**Changements** (.py uniquement):

```diff
+ src/cube.py
+ src/face.py
+ src/main.py
```

## Version 0.0.1

**Message**:\
`🎥 added a triangle and camera`

**Description**:\
Ajout d'un triangle et d'une caméra controllable

**Changements** (.py uniquement):

```diff
+ src/main.py
```

## Version 0.0.0 (restart)

**Message**:\
`✨ first commit`

**Description**:\
Ajout d'une fenêtre et de fichiers informatifs tel que `CHANGELOG.md`, `TODO.md` et `README.md`.\
Ainsi que quelques assets.

**Changements** (.py uniquement):

```diff
+ src/main.py
```
