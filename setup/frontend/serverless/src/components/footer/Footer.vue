<template>
    <span>
        <footer class="page-footer orange lighten-4">
            <div class="container">
                <div class="row">
                    <div class="col m4 s12">
                        <h5 class="black-text thin">About this Library</h5>
                        <p class="black-text">A quick demonstration of lambda + rds + API Gateway + Vue.js.</p>
                    </div>

                    <div class="col m3 offset-m1 s12">
                        <h5 class="black-text thin">Links</h5>
                        <ul>
                            <li v-for="link in links" v-bind:key="link.url">
                                <a v-bind:href="link.url" v-html="link.text"></a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="container black-text">
                    Made by <a class="main-color" href="#">Artur Grigio</a>
                </div>
            </div>
        </footer>
    </span>
</template>

<script>
    import links from '@/components/navbar/links.js';

    export default {
        data: () => {
            return {
                links
            }
        }
    }
</script>
