<template>
 <div class="column is-12">
    <h2 class="title is-8"> What is your worst idea ? </h2>

 <div class="field has-addons">
  <div class="control">
    <input class="input"  type="text" placeholder="Write Here">
  </div>
  <div class="control">
    <a class="button is-info" @click="Next" >
     Submit
    </a>
  </div>
</div>

</div>
</template>

<script>
export default {
    name:'WorstThought',
    data() {
        return{

        }
    },
    methods:{
        Next() {
            this.$router.push('/dashboard/addcubing')
        }
    }
  
}
</script>
