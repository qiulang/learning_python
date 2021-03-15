[How do you split your time when you are a product owner and a software architect?](https://softwareengineering.stackexchange.com/questions/423303/how-do-you-split-your-time-when-you-are-a-product-owner-and-a-software-architect) 我这个问题不仅被关闭，被down-vote 还有 delete-vote 我只能自己留个记录



I can't find a proper term to describe my role, basically it is a product owner and a software architect role combined. I have final say for both product and technical decision.

The Product owner role as in scrum and more. When I do my product owner role, I **get** (without using other fancy word) requirement from my customers; I manage the product backlog, decide the priorities, decide which feature/requirement goes in which release. In a word I decide the product roadmap (of course, work with my team).

I also take the software architect role and make the most important technical decisions. For example, decide which tech stack for frond-end (we chose vue over react); decide whether to use nodejs or php/laravel for back-end (we chose to use both for different features), and design the most important database designs.

I don't want my question and potential answers dwell on scrum, like "you shouldn't do that; you don't do scrum right", because it is the reality in my company. As far as I know it is quite common here in China, especially for start up company. All I can say every practice has pros and cons. One of advantages of taking these 2 roles together is that I can know whether a requirement is doable or not. And to delegate is the key to do both roles right.

So my question is **does anyone have any experience in taking these 2 roles together? How do you split your time in doing both. Is there any best practice?**

PS, there are many reasons I don't want my question to focus on scrum except it is already a reality. The other reasons include (a) I already posted a scrum question here [How do I prevent Scrum from turning great developers into average developers?](https://softwareengineering.stackexchange.com/questions/410482/how-do-i-prevent-scrum-from-turning-great-developers-into-average-developers) I do not want to debate with others about what is scrum's way (b) I feel scrum does not operate on technical level, in scrum there is no defined place for an architect. And the so-called self-organized team sometimes goes too far IMHO.

PPS, is there a name for such role? In way I think **product owner** is a good name because I indeed **own** the product, every bit of it. But scrum already uses it without talking about technical side too much, I am looking for other name. Besides, when I see the words like technical manager, engineering manager, product manager without seeing the context I always have no idea what role does.

--- update ---

I don't really understand the mindset of delete vote. The question was close and that is not enough for you ?



仅有的一个回答



This is an interesting question about balancing potentially conflicting interests:

- Product owner is a role more than a person. As a product owner you want to prioritize the features that have most value for the users.
- Architect is not a scrum role, and architecture belongs to the team. So you have also a role of team member, equal to all the other team members in this capacity. As an architect you want to ensure the most lasting and robust architecture to cope with future evolution.

This leads to two major conflicts of interests (i.e. you’re biased in one role because of the other role):

- as product owner you want features early. As architect you want the foundations of the architecture first, which might require delaying some interesting features that do not fit with the challenges of the architecture.
- for the other team members it‘s not clear when you speak as product owner and when you speak as a peer team member. At worst the will just consider your viewpoint as not to be challenged (and you lose the collective intelligence of the team), at best it will create conflicts (and oblige you to be clearer about your roles and responsibilities), but affecting morale and team efficiency.

This tension is the most intense at the beginning of the project, since both roles are equally sollicitated. In my own experience you should divide time with some discipline, dedicating at least 2/3 for product ownership. Because insufficient time to take this responsibility endangers all the team and the value of its deliverables!

One trick is to allocate most time as product owner, a minimum time for the role as team member, and keep a free buffer to be allocated in priority to product ownership.

The conflicting situation decreases quickly once a stable architecture emerges. It is then not difficult to dedicate most of the time to product ownership. But you need to be aware of your own bias that might lure you away from product value to architectural perfection. It might remain until the end.



@Qiulang I dont’t think it is stupid. In fact it’s really interesting. I once was in a similar situation. It makes job really difficult until you take a deep breath and analyse the situation rationally. Personally, I ended up finding another team member with the required skills to let me fully concentrate on ownership role. It’s possible that some close votes think it’s opinion based (which it is not if one analyses by role). But don’t worry: don’t take downvotes or close votes as personal.



问题被人编辑后 重新允许被回答 [How do you split your time when you are a product owner and a software architect?](https://softwareengineering.stackexchange.com/questions/423303/how-do-you-split-your-time-when-you-are-a-product-owner-and-a-software-architect)

我把另一个问题问在  https://workplace.stackexchange.com/questions/170522/is-there-a-well-established-name-for-a-role-taking-the-technical-and-product-own

