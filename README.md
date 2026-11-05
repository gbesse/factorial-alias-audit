# factorial-alias-audit

## Français

Révéler les effets confondus dans un plan expérimental.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m factorial_alias_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Construit colonnes d’interactions et produits scalaires exacts ±1 ; montre par témoin les effets impossibles à distinguer avant de lancer des essais coûteux.

### Limites

Plans à deux niveaux seulement, interactions jusqu’à ordre3 ; pas d’optimisation de plan ni estimation causale.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Expose aliased effects in an experimental design.

Synthetic data; no network access or secret required.

```sh
python -m factorial_alias_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Builds interaction columns and exact ±1 dot products; witnesses effects that cannot be distinguished before running expensive experiments.

### Limits

Two-level designs only, interactions through order3; no design optimization or causal estimation.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Revelar efectos confundidos en un diseño experimental.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m factorial_alias_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Construye columnas de interacción y productos escalares exactos ±1; muestra efectos indistinguibles antes de ensayos costosos.

### Límites

Solo diseños de dos niveles, interacciones hasta orden3; sin optimización de diseño ni estimación causal.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.itl.nist.gov/div898/handbook/pri/section3/pri3343.htm
