---
name: better-ai-design
description: >-
  Create distinctive websites and app interfaces using broad exploration,
  ambitious creative direction, independent visual critique, generated imagery
  and motion, and deliberate subtraction. Triggers on "better AI design",
  "distinctive UI", "ambitious design direction", "design critique loop",
  "world-class designer", "make this look less AI", "seed string design",
  or requests for bolder, less generic interface design.
---

# Better AI Design

## Goal

Guide the design through three stages—Discover, Define, and Deliver—so the
result feels distinctive and useful rather than predictable. Start with the
feeling the design should create, push beyond familiar choices, then use
judgment to make the result coherent.

## When to Use

Use this skill when the user:

- Asks for a distinctive, ambitious, or less generic website or app interface.
- Wants broad creative exploration before settling on a layout.
- Requests an independent visual critique loop, generated imagery, or advanced
  motion as part of design work.
- Mentions turning AI into a stronger designer, or avoiding default AI aesthetics.

Example prompts:

> Design this landing page with a bold, distinctive direction—not the usual AI look.

> Explore ambitious design languages for this product before we build.

> Run a design critique loop on the current UI until it feels studio-quality.

## Workflow

Guide the design through three stages:

1. **Discover:** Explore possibilities and develop an ambitious direction.
2. **Define:** Give that direction a distinctive identity and improve its execution.
3. **Deliver:** Remove weak or unnecessary elements and polish the result.

Start with the feeling the design should create. Push beyond predictable choices, then use judgment to make the result coherent and useful.

The techniques below support these stages. Random seeding, generated imagery, and video are available approaches—not requirements for every design.

### Discover: Explore the possibilities

Go broad before going deep. The purpose of exploration is to discover a compelling direction, not immediately settle into a familiar layout.

#### Technique 1: Use seed strings to inject variety

Use this technique when seeking fresh starting points or when repeated attempts produce similar results.

Simply asking for something “unique” or “random” can still produce familiar choices. Introduce an external source of variation:

1. Generate a long, random alphanumeric string using a shell script or another execution tool.
2. Examine the string for patterns, sequences, numbers, or other associations that suggest a creative direction.
3. Use those associations to inspire choices such as color, layout, and typography.
4. Apply design judgment to turn the inspiration into a coherent result.

The string is only an inspiration source. Do not display it in the interface.

A varied starting point is not a finished design. Continue developing its identity in the Define stage.

#### Technique 2: Develop more ambitious prompts

Give the design a specific, imaginative premise.

Draw inspiration from a video game, an interior design style, an art installation, or another world with a strong visual character. Describe how that inspiration should influence the experience.

Examples from the article include:

- A productivity landing page whose sections feel like scenes from a pixel-art game.
- An isometric living city where buildings or neighborhoods represent product features.
- A radically asymmetric composition with dissonant colors, unusual typography, and uncomfortable negative space.

The premise should push the design beyond its usual choices while still allowing it to function as the requested product or page.

##### Find the direction with the user

Follow this sequence:

1. **Present many brief ideas.** Keep descriptions short and intentionally open-ended. Their purpose is to spark the user’s imagination, not fully specify every concept.
2. **Invite reactions to favorites.** Ask what the user pictures, what feels appealing, and what feels wrong.
3. **Refine using those reactions.** Develop the elements that resonate and remove the interpretations the user dislikes.
4. **Repeat until the direction feels right.**
5. **Write a concise build prompt** for an initial proof of concept.

A useful exploration prompt:

> Suggest a broad range of bold design languages for this product. Keep each description short and high-level so there is room to imagine it. Explore widely before developing details.

Specific reactions matter more than simply selecting a concept.

For example, an “industrial control panel” direction might become sharper through feedback such as:

- Make it tactile, with satisfying buttons and sound.
- Avoid a cartoonish or overly literal interpretation.
- Use consistent components and restrained details.
- Explore texture and color instead of relying on dull gray gradients.

Carry those preferences into the build prompt. Do not discard them and return to a generic interpretation of the concept.

##### Give difficult ideas a chance

Do not reject an idea solely because it sounds unlikely to work. Build an experiment and judge the result.

If it fails, try another direction. Preserve unsuccessful prompts so they can be revisited as model capabilities improve.

### Define: Deepen the design’s identity

Treat the initial design as a starting point.

A different palette or font can still sit on top of a familiar composition. Look for opportunities to give the design its own personality through structural and detailed choices while retaining its overall aesthetic.

#### Technique 3: Create an independent design-critique loop

Separate implementation from visual judgment.

The implementing agent knows its code, prior decisions, and effort. Use a separate critic to evaluate what is actually visible.

##### Run each iteration

1. Capture a screenshot of the current design.
2. Start the critic in a fresh context.
3. Give it the screenshot and, when available, reference images.
4. Exclude code, implementation details, earlier critiques, and previous iteration history.
5. Request specific feedback and a score.
6. Have the implementing agent revise the design.
7. Capture the revised result and repeat with a fresh critic context.

Use the same critic prompt across iterations.

##### Critic prompt

> Evaluate the aesthetic this design is pursuing. Imagine how a top design studio would execute that aesthetic, then identify the biggest gaps between this screenshot and that standard.
>
> Examine both the overall structure and composition and the fine details.
>
> Penalize patterns that feel overdone, excessive, or obviously AI-generated.
>
> Give concise, specific feedback. Be bold and opinionated rather than limiting recommendations to safe or easy changes.
>
> Finish with a score out of 10 for how closely the design approaches that studio-level standard.
>
> If reference images are provided, use them as a quality baseline or moodboard, not as designs to copy.

##### Make the quality standard concrete

Visual examples provide a clearer standard than an instruction such as “make it beautiful.”

Use comparable professional designs, references the user likes, or generated concept art to demonstrate the intended level of execution.

For a more concrete comparison, present four professional examples alongside the current design and ask the critic to rank all five by polish and taste.

##### Bound the loop

Begin with one or two iterations. Check whether the feedback and results are converging before extending the loop.

The article’s example targets an independent score of at least 9/10. Keep that target out of the critic prompt so it does not influence the score.

Do not pursue the number through an unbounded loop. If improvement stalls, reconsider the direction or quality criteria before spending more iterations.

##### Assign models by role

When model choice is available:

- Use a strong model for the critic’s visual judgment.
- Use a faster or less expensive model for implementation, provided it can execute the direction well.

Keep the critic focused on judgment and the implementer focused on carrying out the improvements.

#### Technique 4: Use image generation to enrich the design

Actively consider generated imagery when the design needs more personality.

Do not settle automatically for gradients, geometric shapes, or basic patterns simply because they are easy to produce in code.

Generate imagery that supports the chosen aesthetic. Consider combining it with shaders or 3D effects when that creates a richer result.

A useful instruction:

> Add personality through generated imagery. Consider combining images with shaders or 3D effects where they strengthen the design. Verify the result in the browser, including individual frames when effects are animated.

Use an available image-generation tool or service. Keep generation credentials local and out of shipped code. If credentials are needed, use a separate key with a restricted spending limit and store it in a gitignored local file.

#### Technique 5: Use video generation for advanced motion

Consider video generation for both animated graphics and transitions between interface states.

Choose suitable available models for the required effects. A service offering multiple models can make it easier to compare options without separate integrations.

##### Create animated graphics

1. Generate a looping clip against a solid-color background.
2. Remove the background with chroma keying or, for more complex footage, a video-matting model.
3. Layer the resulting animation into the interface.

For glass-like effects, render the object against the page’s background colors before removing the background. This can preserve the appearance of reflections and refraction within the generated object.

The article’s example uses a crystal that splinters and slowly rotates, with glassy reflections, light, and shadows.

##### Create transitions between states

Use video interpolation to connect product stills or interface states.

1. Generate the initial frame.
2. Generate a clip that transitions from that frame into the next state.
3. Use the clip’s final frame as the starting point for the following transition.
4. Connect the clips into a continuous sequence.
5. Play or scrub the sequence in response to navigation, scrolling, or swiping.

Match the motion to the interaction.

The article’s scrolling example follows a suitcase through three states:

- Floating above the floor.
- Landing and opening.
- Receiving its contents from above.

Choose a model suited to physical motion and visual consistency. Inspect the transitions frame by frame to verify continuity.

### Deliver: Polish through subtraction

#### Technique 6: Remove elements that do not add value

Once the design has a strong identity, focus on what should disappear.

Review whether the design makes sense, flows well, and serves the user’s practical purpose. Do not assume that adding more will improve it.

Look for:

- Text that explains what the visuals already communicate.
- Extra labels and unnecessary space.
- Arbitrary colors or highlights.
- Glows and gradients that do not strengthen the aesthetic.
- Containers that add structure without adding value.
- Custom controls that are less effective than appropriate native components.

Remove or simplify these elements.

The article’s calorie-tracker example improves by moving toward an image-centered grid, removing excessive decoration and containers, using native controls, and tightening the text.

Use that example as an exercise in restraint, not a requirement that every design adopt the same appearance.

Let the strongest elements carry the experience. Preserve the design’s personality while reducing everything that distracts from it.

## Guardrails

- Never display seed strings or inspiration artifacts in the shipped interface.
- Never put image-generation or video-generation credentials in shipped code;
  keep keys local, gitignored, and spending-limited when used.
- Never run an unbounded critique loop; start with one or two iterations and
  stop when improvement stalls.
- Never put the target score inside the critic prompt.
- Never feed the critic code, implementation details, earlier critiques, or
  prior iteration history—screenshots and optional references only.
- Never discard specific user reactions and fall back to a generic reading of
  the chosen concept.
- Never treat seed strings, generated imagery, or video as mandatory for every
  design—use them when they strengthen the result.
- Never reject a difficult idea solely because it sounds unlikely; build a
  small experiment and judge the result.
- Report failures (missing tools, stalled critique, broken motion) rather than
  silently substituting a generic layout.

## Completion Checklist

- [ ] Explored multiple directions before locking a familiar layout.
- [ ] Direction was refined with the user (or an explicit solo brief) into a
      concise build prompt.
- [ ] Initial proof of concept expressed a specific imaginative premise, not
      only a palette/font swap on a stock composition.
- [ ] When critique was used: fresh critic context, screenshot-only input, same
      critic prompt, and a bounded iteration count.
- [ ] When imagery or video was used: credentials stayed local; results were
      verified in the browser (including frames for animation).
- [ ] Deliver pass removed redundant text, decoration, containers, and weak
      custom controls without erasing the design’s personality.
- [ ] Final result is distinctive, coherent, and still usable as the requested
      product or page.

## Source

Adapted from Anshu Chimala’s
[“How to turn your AI into a world-class designer”](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world).
