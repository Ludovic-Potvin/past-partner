Straight copy and past from https://github.com/makerforgetech/modular-biped/wiki/Software

## What does it do

Only module with coupling, pubsub task is to create a observer base pattern in the application.

Module will publish and subscribe to event to act accordingly. This allow the robot modules to emit event and react to event according to the config we give them. Giving us full control on where they also connect.

Ideally, pubsub would act as a core feature used by every other part of the project.