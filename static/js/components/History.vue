<template>
<div id="history">   
  <div class='container' > 

    <table class="table table-hover">

      <thead class="thead-inverse">
       <tr>
         <th><h4>#</h4></th>
         <td ><h4>Date</h4> </td>
         <td ><h4>Opponent</h4></td>
         <td ><h4>Score</h4></td>
         <td ><h4>Result</h4></td>
       </tr>  
      </thead>

      <tbody>
        <tr v-for="LogGame in lista">
          <th scope="row">{{LogGame.pk}}</th>
          <td >{{ LogGame.fields.game_date }}</td>
          <td v-for="Users in listaU"  v-if='Users.pk==LogGame.fields.opponent'>{{Users.fields.username}}</td> 
          <td >{{ LogGame.fields.yourScore }}-{{ LogGame.fields.opponentScore }} </td>
          <td v-if='LogGame.fields.opponent<LogGame.fields.yourScore'>winner</td>
          <td v-else>loser</td> 
        </tr >
      </tbody>
    </table>
  </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      sortDirection: 'desc',
      lista: [],
      listaU: []
    }
  },
  mounted() {
    this.$http.get("/homepage/games").then( (req) => this.lista = req.data )
    this.$http.get("/app/users").then( (req) => this.listaU = req.data )
  },
}  
</script>
