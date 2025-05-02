
## Clean comment on the design pattern for the app
https://www.reddit.com/r/robotics/comments/gp5cvg/any_resources_for_design_patterns_in_robotic/
ROS is already implementing a lot of design patterns.

Some of them are microservices type patterns, such as:

- The node pattern (every system component should be a different node; helps with the separation of concerns and allows to easily swap components with different implementations)
    
- Communication patterns
    
    - publisher/subscriber pattern (send message to whoever is interested; loosely couples sender and receiver of messages)
        
    - service pattern (send a message to a specific component and get a response from it)
        
- External configuration pattern (components have externally configurable behavior to adapt to the specific environment)
    
- Service discovery pattern (which you don't need to worry about)
    
- etc...
    

Having said that, probably all microservice design patterns can be applied to ROS as well. I can't recommend any particular book on microservice design patterns though (anyone?).

A few patterns implemented in ROS are specific to robotics (e.g. action pattern - much like the service pattern but with continuous feedback about the progress of the task), etc... I don't know any books specifically about robotics design patterns though.

Since ROS is a system that connects multiple components, [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html) can be applied. For example, the main node you refer to could be implemented with the Process Manager Pattern (execute a configurable flow of steps). The Aggregator pattern comes up as you often need to aggregate sensor data, etc....

Of course the basic [Gang of Four patterns](http://www.blackwasp.co.uk/gofpatterns.aspx) often come in handy.

HOWEVER

Even applying all patterns in the world will not make your design infinitely flexible. Moreover, these design patterns, like many other things, are tools - they can help you do things quickly or they can slow you down and cost you greatly.

For example, implementing your main node as a Process Manager would be a great amount of effort to do yourself and, although it will give you the flexibility to change the workflow through configuration, you rarely need such a functionality especially given the cost.

That is not to say that learning design patterns is a waste of time - on the contrary - they will be of great help guiding you on how to design your software better. I wouldn't say, however, they're critical (especially given ROS has already layed out the main architecture for you).

In essence, the best you can do design-wise is the simplest possible thing that works now and then, break down/upgrade the design as you go (when you see how your program evolves). Of course, the sooner you identify something will change in the future (e.g. the way you've identified you'll probably upgrade your LIDAR), the better you can plan for it and plant extension points in your design.

When it comes to robotics, "a single software component per hardware component with higher-level components leveraging on the lower level ones" type of architecture is usually sufficient (or at least a good start).

BTW, always check if there's something out there you can reuse. ALWAYS. The ROS ecosystem offers a lot of stuff as I'm sure you know. For example, for your particular case - if your main node is similar to a state machine, check out the [Smach ROS node](http://wiki.ros.org/smach/Tutorials/Getting%20Started) - it's a generic state machine ROS node. I haven't used it myself though.

TLDR:

- Ros already lays out the main software architecture for you.
    
- A single software component per hardware component with higher-level components leveraging on the lower level ones is usually sufficient design.

## Good github to find info on robot (built his own)

https://github.com/makerforgetech/modular-biped/wiki/Software