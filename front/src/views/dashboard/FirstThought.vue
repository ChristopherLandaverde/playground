<template>

<div class="column is-12">

<h2 class="title is-8"> What problem are you trying to solve today?</h2>


<div class="field has-addons">
  <div class="control">
    <input class="input" v-model="name.name" type="text" placeholder="Write Here">
  </div>
  <div class="control">
    <a class="button is-info" @click="submitFirst">
      Next Level
    </a>
  </div>
</div>



</div>
            






</template>

<script>
import axios from 'axios'


export default {
    name:'FirstThought',
    data(){
        return {
             name:{},
    
            
        }
    
    },
    mounted (){

  
    },
    methods:{

        submitFirst() {
                axios
                .post('api/v1/firstthoughts/',this.name)
                .then(response =>{
                    console.log(response)

                    
                })
                 this.$router.push('/dashboard/rapididea')
        },
       
           

            
        
    }
}
</script>
