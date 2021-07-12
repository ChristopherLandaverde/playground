<template>
  <div class="about">
 <section class="hero is-white is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns  is-vcentered reverse-columns">
          <div class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-5-desktop is-offset-1-desktop
          is-5-widescreen is-offset-1-widescreen
          is-5-fullhd is-offset-1-fullhd" data-aos="fade-down">
            <h1 class="title titled is-1 mb-6">
              A playground for the mind
            </h1>
            <h2 class=" subtitled subtitle has-text-grey is-4 has-text-weight-normal is-family-sans-serif">
           This the mental gym for you to work out your ideas and challenges your thoughts.
            </h2>
            <div class="buttons">
               <router-link :to="{ name: 'LogIn'}" class="button is-black"> Login</router-link>
               <router-link :to="{ name: 'SignUp'}" class="button"> Sign-up</router-link> 

            </div>
          </div>

          <div data-aos="fade-right" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-4-desktop is-offset-1-desktop
          is-4-widescreen is-offset-1-widescreen
          is-4-fullhd is-offset-1-fullhd">
            <figure class="image is-square">
              <img src="../assets/1.png" width="202" height="100">
            </figure>
          </div>

        </div>
      </div>
    </div>
  </section>

  <section class="hero is-white is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns  is-vcentered">
          <div data-aos="fade-left" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-4-desktop is-offset-1-desktop
          is-4-widescreen is-offset-1-widescreen
          is-4-fullhd is-offset-1-fullhd">
            <figure class="image is-square">
              <img src="../assets/2.png">
            </figure>
          </div>
          <div data-aos="fade-down" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-5-desktop is-offset-1-desktop
          is-5-widescreen is-offset-1-widescreen
          is-5-fullhd is-offset-1-fullhd">
            <h1 class="titled title is-1 mb-6">
              Brainstorms
            </h1>
            <h2 class="subtitled subtitle">
              choose a topic, develop an approach to a topic, or deepen your understanding of the topic’s potential.
            </h2>
          </div>

        </div>
      </div>
    </div>
  </section>

  <section class="hero is-white is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns  is-vcentered reverse-columns">
          <div data-aos="fade-right" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-5-desktop is-offset-1-desktop
          is-5-widescreen is-offset-1-widescreen
          is-5-fullhd is-offset-1-fullhd">
            <h1 class="title titled is-1 mb-6">
             Inversions
            </h1>
            <h2 class="subtitle subtitled">
         By simply thinking about what you want to avoid or the opposite of what you want to achieve, you can plan effectively to prevent failure.
            </h2>
          </div>
          <div data-aos="fade-down" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-4-desktop is-offset-1-desktop
          is-4-widescreen is-offset-1-widescreen
          is-4-fullhd is-offset-1-fullhd" >
            <figure class="image is-square">
              <img src="../assets/3.png">
            </figure>
          </div>

        </div>
      </div>
    </div>
  </section>

   <section class="hero is-white is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns  is-vcentered">
          <div data-aos="fade-left" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-4-desktop is-offset-1-desktop
          is-4-widescreen is-offset-1-widescreen
          is-4-fullhd is-offset-1-fullhd">
            <figure class="image is-square">
              <img src="../assets/4.png">
            </figure>
          </div>
          <div data-aos="fade-down" class="column
          is-10-mobile is-offset-1-mobile
          is-10-tablet is-offset-1-tablet
          is-5-desktop is-offset-1-desktop
          is-5-widescreen is-offset-1-widescreen
          is-5-fullhd is-offset-1-fullhd">
            <h1 class="titled title is-1 mb-6">
              Cubing
            </h1>
            <h2 class="subtitled subtitle">
              Cubing is a tool to look at one thing from six (each side of a cube) different way
            </h2>
          </div>

        </div>
      </div>
    </div>
  </section>
  </div>
</template>

<style scoped>
  @media(max-width: 500px) {
      .reverse-columns {
        flex-direction: column-reverse;
        display: flex;
      }
    }

    .titled {
      font-family: 'Merriweather', serif !important;
      font-size: 58px !important;
      font-weight: 400 !important;
      line-height: 64px !important;
    }

    .subtitled {
      font-family: 'Merriweather', serif !important;
      font-size: 22px !important;
      font-weight: 400 !important;
      line-height: 36px !important;
    }
</style>

<script>

</script>
