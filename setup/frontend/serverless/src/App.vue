<template>
  <div id="app">
      <navbar></navbar>
      <router-view/>
      <vfooter></vfooter>
  </div>
</template>

<script>
    import navbar from '@/components/navbar/Navbar.vue';
    import vfooter from '@/components/footer/Footer.vue';

    export default {
      name: 'app',
      components: { navbar, vfooter }
    };
</script>

<style>
    .no-margin {
        margin: 0px !important;
    }
    .no-padding {
        padding: 0px !important;
    }
    .thin {
        font-weight: 100 !important;
    }
    .spacer-1 {
        height: 10px !important;
    }
    .spacer-2 {
        height: 20px !important;
    }
    .spacer-4 {
        height: 40px !important;
    }
    .inline {
        display: inline-block !important;
    }
    .main-color {
        color: #0064a4;
    }
    .main-background {
        background-color: #5c9be5;
    }
    .secondary-color {
        color: #ffd300 !important;
    }
    .secondary-background {
        background-color: #ffd300;
    }
    @media only screen and (min-width: 1200px) {
        html {
            font-size: 18px;
        }
    }
</style>
