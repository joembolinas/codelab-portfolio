
<div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
  <img src="https://www.gstatic.com/devrel-devsite/prod/v5e941f15ff6710591bee254538202655020220785b40a3f4d932e94adb9f6037/codelabs/images/lockup.svg" alt="Google Codelabs Logo" width="620">
  <h1>Google Codelabs</h1>

</div>

<div class="about-card"><h2 class="title">About this codelab</h2><div class="last-updated"><i class="material-icons">subject</i>Last updated Sep 4, 2026</div><div class="authors"><i class="material-icons">account_circle</i>Written by Luke Schlangen</div></div>

---

<table width="100%" style="width: 100%; border-collapse: separate; border-spacing: 8px; table-layout: fixed;">
  <tr>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="01-Introduction.md"><strong>01-Introduction</strong></a>
    </td>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="02-Project_Setup.md"><strong>02-Project_Setup</strong></a>
    </td>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="03-Create_Portfolio.md"><strong>03-Create_Portfolio</strong></a>
    </td>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="04-Test_and_Iterate.md"><strong>04-Test_and_Iterate</strong></a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="05-Deploy_to_Cloud_Run.md"><strong>05-Deploy_to_Cloud_Run</strong></a>
    </td>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="06-Add_custom_domain.md"><strong>06-Add_custom_domain</strong></a>
    </td>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="07-Clean_Up.md"><strong>07-Clean_Up</strong></a>
    </td>
    <td align="center" width="25%" style="padding: 14px 8px; border: 1px solid #dadce0; border-radius: 8px; background-color: #f8f9fa;">
      <a href="08-Conclusion.md"><strong>08-Conclusion</strong></a>
    </td>
  </tr>
</table>

---

## Learn More

Visit [this link](https://developers.google.com/profile/badges/builder/milestone1/award?authuser=1) to claim the **Completed Builder Journey** badge!

To continue your journey, head to [goo.gle/builders](https://goo.gle/builders) for your next lab.i

[^1]: Hi, I'm Luke schlangen and today I'm
 going to walk through our lab launch your portfolio
 website with AI.
 This is one in a series of labs for getting
 started for AI builders.
 And this lab will do exactly that.
 We're going to launch your portfolio website with AI.
 So we'll cruise through the introduction here.
 But essentially what we're going to be doing today
 is using AI Studio's build mode to rapidly prototype
 a front end using natural language.
 So that is English in my case.
 So we're going to go to our project setup.
 This part does take a little bit of effort
 if you've never used a Google Cloud project before,
 but this could be different.
 Whether or not you are able to get on the starter tier
 or you want to do a standard deployment.
 So I'm going to skip this step.
 Maybe I'll make a separate video for billing specifically
 if you'd like to see some of that.
 But we're going to dive right into the fun
 part, which is going to the AI Studio apps panel.
 So you can get here a couple of different ways.
 One quick way is to click this link, this AI Studio apps panel.
 Another is to go to AI dev.
 So I will bring you straight to AI Studio.
 And it might bring you to the playground.
 But where we're going to be today is in this new app panel.
 But one thing that I think is really cool
 is in all of these labs, we have this.
 This link will automatically fill in the prompt box for you,
 and you can click that link, and it will automatically
 fill in the content that we had before.
 So if you're new to building software,
 this should be very quick to get up and running.
 If you've got a Google account, you've
 got access to these tools.
 We can get you started here.
 Now all that our model can do is act based on the information
 we've given it.
 So we've told it to build a personal portfolio
 website for us.
 This site should have a modern responsive design and sections.
 You can tailor this to what you want.
 So all of these builder labs are meant to be kind of open
 ended, where you can add and you can remove.
 And regardless of whether or we're
 using the same exact prompt, we're
 probably going to get different outputs.
 This is called non-determinism in AI.
 Essentially, it's a little bit of randomness in the system.
 If you've heard of temperature, it's
 also like adjusting that randomness,
 but there's always some level of randomness in this.
 So here it says my professional profiles,
 but it doesn't know who I am.
 So at this point, you can make a couple of different choices.
 You can decide that you want to give it
 a little bit more information.
 What some folks do is they upload their resume.
 I already have a website that I'd
 like it to be based on so I'm going to say based on Luke
 for my personal branding.
 Sure, I like that I don't actually
 need a contact page or a blog page yet.
 I'm going to keep it just to this.
 So I'm going to say use Luke for my personal branding.
 And I'm just going to add my name is Luke.
 So that's unique enough where it can probably find me online
 and figure out those details.
 So let's go ahead.
 This is GitHub LinkedIn I think that's enough information for it
 to pull in what it needs.
 So let's let it run.
 One thing that's neat is as it's running,
 it actually gives me a couple of different options for how
 I would like this to look.
 One thing I want to call out from a technical perspective
 is that while these are very neat,
 and I do actually very much like this bold typography one,
 if you select the design, what it does
 is essentially cues another prompt.
 And that means basically you've got another prompt
 that will run as soon as the initial version of your site
 is complete.
 So since I'd like to move quickly through this demo,
 I'm going to say skip for now and stick with whatever
 is initially designed for me.
 And there we go.
 Now we've got the first iteration of my application all
 ready to go.
 So let's go back to the next step in the lab.
 It says test and iterate.
 So I have been fortunate enough here where
 I don't see any errors popping up right away,
 but I'm going to test to see if this is working.
 So this says your name.
 Let's try sending a message.
 My name here is going to be tester
 and my email address is going to be tester <user@example.com>.
 And it's how are you doing.
 And I'm going to click Send message
 and it says it was sent successfully.
 I am curious what that means because I don't know how it
 would have received something.
 So this is maybe a great UI for this,
 but I don't actually see the functionality behind it.
 Now, for those who do want to jump into the code,
 you can go into the code and you can make these changes yourself.
 But what I would like to do is remove this section here.
 I would like to remove this send a message section because I
 don't think that this is actually functionally working.
 So I'm going to say let's remove.
 The ask age and contact sections of this profile.
 And this isn't to say that you need to do this.
 The whole point of this builder experience
 is that you get to build what you
 want to build as it does this.
 It runs into issues.
 It notices those issues and it fixes those problems.
 The next version of my website seems like it's ready to go.
 Let's take a look.
 And so it says I'm a principal Cloud systems engineer.
 That is not fully accurate.
 I am a senior full stack developer,
 but I did not go and work at apex digital systems,
 so this would probably require more context in order for it
 to get this information right.
 Maybe I should have uploaded my resume in order
 to get this information, although it does
 have Minneapolis, Minnesota.
 So it's figured out where I am with this.
 Let's say that I'm ready to deploy this to the world.
 I can now click Publish.
 And say get started and I can pick
 which application I would like to have this deployed to.
 I'm going to deploy to full stack improv, which
 is my site for just about everything
 that I'm coming up with on the spot.
 And here is something really cool.
 Here we've got a Studio.
 You can actually change this.
 Adapt this to what you would like.
 So I'm going to see Luke portfolio Studio.
 There it is publish app.
 And now it is publishing.
 After a few minutes, it will be a live URL
 that anyone in the world can see.
 And there we have it.
 We have it deployed application or at least
 it says it's deployed.
 Let's go ahead and click Visit.
 So when I click Visit I see hi I'm Luke schlangen. Fantastic
 and here this is a live URL Luke schlangen portfolio
 Studio where anyone in the world can come and see
 what I've built today.
 So this is the mentality behind this builder lab.
 And we have completed the steps of the lab this deploy
 to Cloud Run.
 Additionally, if you'd can say add a custom domain.
 So if you'd like it to be deployed at a domain that is not
 Luke schlangen portfolio Studio, these ones are vanity domains.
 They are special personalized custom domains
 that do all end in a Studio.
 But if you'd like to add a more specific domain
 name to your application, you can do that
 and these steps will walk you through that.
 Do leave a comment in the video if you
 would like me to walk through those steps at some point
 so that you can see how do I deploy my application
 to a custom domain.
 With that might want to clean up your application
 if you don't want that portfolio site to be live.
 These are the steps to do that.
 And at the end, I would strongly recommend
 if you are badge motivated as I am to claim your badges.
 So go to that conclusion step.
 And then there's even another badge
 a very pretty little badge.
 Will it show up.
 There it is.
 Yes so this says you earned the completed builder journey badge.
 And you can get that on the last step of this lab.
 So if you stayed all the way to this point in the video,
 make sure you do that on the lab as well.
 Thank you so much for following along.
 If you've made it this far, I really
 appreciate you watching all the way to the end,
 and I hope you have fun on build your journey.
 Please ask questions.
 What would you like to learn next.
 Leave that in the comments below.
 Happy building.
 
 ---
