<template>
  <div id="main" class="main">
    <form>
      <input
        v-model="username"
        type="text"
        placeholder="name"
        autocomplete="false"
      />
      <button v-on:click.prevent="fun" type="button"></button>
    </form>
  </div>
</template>

<script>
export default {
  name: "main",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    fun() {
      localStorage.setItem("username", this.username);
      this.$router.push("/chat"); // this.$router.push({path:"/chat"}|{name:"chat"})
    },
  },
};
</script>

<style></style>
