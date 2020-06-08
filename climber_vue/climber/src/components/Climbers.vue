<template>
  <v-row cols="12" sm="10" offset-sm="1">
    <v-col cols="12" sm="10" offset-sm="1">
      <v-card>
        <v-list two-line>
          <template v-for="(item, index) in items.slice(0, 6)">
            <v-subheader v-if="item.header" :key="index"><v-row><v-dialog v-model="dialog_1" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Добавить альпиниста</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Добавить альпиниста</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6">
                <v-text-field label="Имя*" required v-model="first_name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6">
                <v-text-field v-model="last_name"

                  label="Фамилия* "
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="12">
                <v-text-field v-model="address"
                  label="Адрес*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field v-model="age"
                  label="Возраст*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-autocomplete
                  :items="['Певко', 'Пипсы', 'Сериальчек', 'Вьюшечка', 'MLHack', 'Etersoft', 'Writing', 'Coding', 'Basejump']"
                  label="Покоренные вершины"
                  multiple
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>*Обязательные для заполнения поля</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog_1 = false">Закрыть</v-btn>
          <v-btn color="blue darken-1" text @click="submit">Добавить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog></v-row></v-subheader>
            <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>
            <v-list-item v-else :key="item.id" id="item.id" @click="dialog_3">
              <v-list-item-avatar>
                <img :src="item.avatar">
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="item.first_name + ' ' + item.last_name"></v-list-item-title>
                <v-list-item-subtitle v-html="item.address"></v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action><v-icon>mdi-pencil</v-icon></v-list-item-action>
            </v-list-item>
          </template>
        </v-list>
      </v-card>
    </v-col>
    <v-dialog v-model="dialog_3" persistent max-width="600px">
    <v-card>
        <v-card-title>
          <span class="headline">{{ item + "sdsd" }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Legal first name*" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Legal middle name" hint="example of helper text only on focus"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Legal last name*"
                  hint="example of persistent helper text"
                  persistent-hint
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Email*" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Password*" type="password" required></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-select
                  :items="['0-17', '18-29', '30-54', '54+']"
                  label="Age*"
                  required
                ></v-select>
              </v-col>
              <v-col cols="12" sm="6">
                <v-autocomplete
                  :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                  label="Interests"
                  multiple
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>


</template>

<script>

  import {indexOf} from "../../../../../../../../Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/notebook/static/components/codemirror/src/util/misc";

  export default {

    mounted() { this.get_climbers()

    },
    name: 'Climber',
    data () {

      return {
      a:200,
      dialog_1: false,
      dialog_2: false,
      dialog_3: false,
      first_name: '',
      last_name: '',
      age: 0,
      address: '',
      radios: 1,
      items: [
       ]
    }
    },
    methods: {
      get_climbers() {
      function randomInteger(min, max) {
        let rand = min + Math.random() * (max + 1 - min);
        return Math.floor(rand);
      }
        this.axios
          .get(`http://127.0.0.1:8000/api/climber/list`)
          .then(response => { this.items = response.data;
          // this.items.avatar = url && console.log(url);
            for(let i=0; i<this.items.length; i++){
              if (i<1){
                this.items[i].header = 'Альпинисты';
              }
              else {
                let url = 'http://placekitten.com/' + randomInteger(350, 600) + '/' + randomInteger(150, 400);
                this.items[i].avatar = url;
              }
            }

          })
          .catch(err => { console.error(err) })
      },
      submit () {
      this.axios
        .post('http://127.0.0.1:8000/api/climber/add', {
            first_name: this.first_name,
            last_name: this.last_name,
            age: this.age,
          }
        )
        this.clear();
        this.dialog_1 = false;
    },
      clear () {
        this.last_name = '',
        this.first_name = '',
        this.age = 0,
        this.address = ''
      },
      return_index() {
        console.log(this.items.last_name);
      }
    }
  }
</script>
