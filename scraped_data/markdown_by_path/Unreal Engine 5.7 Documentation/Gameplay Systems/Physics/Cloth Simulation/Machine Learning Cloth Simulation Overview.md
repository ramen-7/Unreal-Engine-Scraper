<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/machine-learning-cloth-simulation-overview?application_version=5.7 -->

# Machine Learning Cloth Simulation Overview

1. ![Epic Games](https://edc-cdn.net/assets/images/logo-epic.svg)[Developer](/)
2. [Documentation](/documentation/ "Documentation")
3. Unreal Engine
   * [Unreal Engine](/documentation/en-us/unreal-engine)
   * [Fortnite](/documentation/en-us/fortnite)
   * [Twinmotion](/documentation/en-us/twinmotion)
   * [MetaHuman](/documentation/en-us/metahuman)
   * [RealityScan](/documentation/en-us/realityscan)
   * [RealityScan Mobile](/documentation/en-us/realityscan-mobile)
   * [Fab](/documentation/en-us/fab)
4. [Unreal Engine 5.7 Documentation](/documentation/en-us/unreal-engine/unreal-engine-5-7-documentation "Unreal Engine 5.7 Documentation")
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Cloth Simulation](/documentation/en-us/unreal-engine/cloth-simulation-in-unreal-engine "Cloth Simulation")
8. Machine Learning Cloth Simulation Overview

# Machine Learning Cloth Simulation Overview

Overview of Machine Learning Cloth Simulation in Unreal Engine.

![Machine Learning Cloth Simulation Overview](https://dev.epicgames.com/community/api/documentation/image/320a329c-7b5e-4991-a572-6a0472de11c3?resizing_type=fill&width=1920&height=335)

 On this page

## Introducing the Machine Learning Cloth Simulation System

The **Machine-Learning (ML) Cloth Simulation** system provides high-fidelity, highly performance, real-time cloth simulation in **Unreal Engine**.

The system provides higher fidelity than the traditional physics-based model by using a trained dataset that can be used in real-time to produce results that were previously only achievable with offline simulation.

### Benefits of Using Machine Learning

In traditional game development, you simulate character clothing by using a physics solver. However, this process can be computationally intensive due to the time-consuming updates for elasticity, and the complicated interactions between cloth and body.

A machine learning system can assist users in training a model using high-quality simulation data generated in advance. This system is capable of producing clothing meshes that are of similar quality to pre-simulated data, while being fast and efficient in terms of memory usage.

## Technical Implementation

For each frame, the ML Cloth Simulation system takes the character's skeletal pose as input and predicts a final cloth pose by deforming a base cloth mesh using linear blend skinning. The deformation has two major components.

The first component is a **low-frequency deformation** similar to the neural morph model.

This component is modeled with a multi-layer perceptron (MLP) network, which predicts a set of coefficients using the Skeletal Mesh pose as input. The low-frequency deltas are computed as:

C++

```
low_frequency_deltas = mean_delta + coeffs * basis
```

low\_frequency\_deltas = mean\_delta + coeffs \* basis

Copy full snippet(1 line long)

The basis can be learned at training time or pre-computed using principal component analysis (PCA).

To train this component, you should prepare a dataset of random poses and simulate clothing to settle on each pose. For this component, we recommend 5000 poses for a humanoid character.

The second component is a **high-frequency deformation** computed using the **Nearest Neighbor** search.

This component takes the coefficients from the first component and applies a nearest neighbor search in a Nearest Neighbor dataset, namely:

C++

```
high_frequency_deltas = NearestNeighborSearch(coeffs)
```

high\_frequency\_deltas = NearestNeighborSearch(coeffs)

Copy full snippet(1 line long)

For this component, one should prepare a small, but diverse set of poses and simulate clothing to settle on each of the poses. Ideally the poses should be taken from some key frames of the animations in-game. For optimal results, between 50 and 100 poses are recommended for a humanoid character.

Using this technique, the vertex delta is calculated as follows:

C++

```
vertex_delta = low_frequency_deltas + high_frequency_deltas
```

vertex\_delta = low\_frequency\_deltas + high\_frequency\_deltas

Copy full snippet(1 line long)

For the trained dataset, you can generate the final cloth position for each pose by using the **Chaos Cloth Generator** tool under the **ML Deformer Editor** in Unreal Engine. This will simulate the cloth and generate a Geometry Cache that can be used in real-time.

Alternatively, you can use external cloth simulation solvers (such as Houdini Vellum). For each pose, simulate the cloth until settlement and save the settled cloth in the Geometry Cache. You can import the cache into Unreal Engine as an Alembic file.

Follow the [ML Cloth Generation tutorial](https://dev.epicgames.com/community/learning/tutorials/PdRX/unreal-engine-ml-cloth-generation) to learn how to generate the Geometry Cache inside Unreal Engine.

For best results, you should manually choose the most relevant poses for the dataset. However, it is possible to do automatic pose selection with the **KMeans Pose Generator**. The generator takes an animation sequence and runs the KMeans algorithm to generate a list of entries for the Nearest Neighbor dataset.

### Current Limitations

The current system implementation has one main limitation — the clothing is assumed to be quasi-static. This means the system can predict shape details like wrinkles but cannot predict dynamic motion like swinging or draping.

This system is currently best suited for tight-fitting clothing like pants and T-shirts, but not loose garments like dresses or capes.

You can learn how to use the ML Cloth system by following the  [ML Deformer - Nearest Neighbor Model](https://dev.epicgames.com/community/learning/tutorials/pwaY/unreal-engine-nearest-neighbor-model-5-4) tutorial on the Epic Developer Community.

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [cloth](https://dev.epicgames.com/community/search?query=cloth)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introducing the Machine Learning Cloth Simulation System](/documentation/en-us/unreal-engine/machine-learning-cloth-simulation-overview?application_version=5.7#introducing-the-machine-learning-cloth-simulation-system)
* [Benefits of Using Machine Learning](/documentation/en-us/unreal-engine/machine-learning-cloth-simulation-overview?application_version=5.7#benefits-of-using-machine-learning)
* [Technical Implementation](/documentation/en-us/unreal-engine/machine-learning-cloth-simulation-overview?application_version=5.7#technical-implementation)
* [Current Limitations](/documentation/en-us/unreal-engine/machine-learning-cloth-simulation-overview?application_version=5.7#current-limitations)
