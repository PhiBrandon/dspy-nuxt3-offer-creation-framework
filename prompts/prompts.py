offer_refinement_prompt = """
Given offer creation checklist and a current service offering. construct an offer using the offer creation checklist, think step by step through the checklist. output 20 concise and engaging offers with explanations. Each offer should be concise, no more than 1 sentence.
Offer Creation Checklist:
# Create Your Core Offer Part 1 & 2

## V. Create Your Offer Components
- Define Their Dream Outcome
- List out Every Possible Problem they can Encounter
  - Every intricate step
  - Everything that happens before and after achieving their goals
  - What next problem will they face
- How can we make it worth it?
- How can we make it easier?
- How can we make it faster?
- How can we make it enjoyable, sustainable, and something they believe they can do?
- List out every possible solution to the problems
  - How to YAY without BOO even if you GREATEST OBSTACLE
- Use Delivery Cube to think thorough ideas

## The "Delivery Cube"
1. Group Ratio
   - 1-1
   - Small Group
   - One to Many
2. Level of Effort On Their Part
   - Do It Yourself (DIY)
   - Done-With-You (DWY)
   - Done-For-You (DFY)
3. Support Levels & Types
   - SMS
   - Chat
   - Email
   - Expert vs Normal
   - Phone
   - Zoom
4. Consumption Types
   - Live/Virtual
   - Recorded
   - In Person
   - Written
   - Audio 
   - Video
5. Speed & Convenience
   - 24/7
   - 9-5 M-F
   - How fast will you reply to questions? Are there levels?
6. 10x to 1/10th test
   - What would I deliver if my product cost 10x its current amount
   - What would I deliver if my product cost 1/10th its current cost and had to provide more value than I currently am at my current price?

## VI. Trim & Stack: Prioritize the solutions based on value & cost. You should have multiple pieces you are stacking together to make the offer more compelling.

### "The Meat & Potatoes" of the Offer
- Core Offer Component #1
- Core Offer Component #2 
- Core Offer Component #3
- Core Offer Component #4
- Core Offer Component #5

- High Value: meaningful, fast, easy, and believe they can do it and enjoy it
- Low value: not meaningful, slow, hard/complex, not interesting and dont believe they'll like it
- High cost: requires people to scale
- Low cost: can scale without people but with up front effort instead
- Remove all items that are NOT high value
- Keep only a handful of High cost high value, and everything else should be high value low cost
- Start with something that is less scalable (more high cost high value) to get people to say yes and begin monetization

Current Offer:
{offer}
"""


offer_grading = """
Given 4 criteria, grading scale for each, and an offer, rate the offer based on the 4 criteria.

Criteria:

Dream Outcome: The end result that is meaningful to the prospect. The better the dream outcome, the more value the person will attach to the product or service.
Grading Scale: On a scale of 1-5, with 5 being the most meaningful and valuable dream outcome to the prospect.

Perceived Likelihood of Achievement: The prospect's belief that they will succeed in achieving the desired outcome by purchasing the product or service. The higher the perceived likelihood, the more valuable the offer becomes.
Grading Scale: On a scale of 1-5, with 5 being the highest perceived likelihood of achievement.

Time Delay: The time it takes for the prospect to see the final result and initial results after purchasing the product or service. The shorter the time delay, the more valuable the offer becomes.
Grading Scale: On a scale of 1-5, with 5 being the shortest time delay between purchase and achieving the desired result.

Effort and Sacrifice: The additional costs and inconveniences the prospect must incur to achieve the desired result. The lower the effort and sacrifice required, the more valuable the offer becomes.
Grading Scale: On a scale of 1-5, with 5 being the lowest effort and sacrifice required from the prospect.
Offer:
{offer}
"""