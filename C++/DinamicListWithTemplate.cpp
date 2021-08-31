#include <iostream>
using namespace std;
template <class T>
class MyList {
private:
    class Cell {
        public:
            T val;
            Cell* prox;
            Cell(const T &x) {
                val = x;
                prox=NULL;
            }
    };
    void Esvazia(Cell *aux);
    void Mostra(Cell *aux);
    bool InsereNaPosicao(const T &num, const int &pos, Cell *aux, const int &posatual);
    Cell *primeiro, *ultimo;
    int tam;
public:
    MyList() {
        tam=0;
        primeiro=ultimo=NULL;
    };
    void Esvazia();
    void Mostra();
    void MostraIterativo();
    ~MyList() {
        Esvazia();
    };
    bool InsereNaPrimeira(const T &num);
    bool InsereNaPosicao(const T &num, const int &pos);
    //bool InsereNoFim(const int &num);
    int size(void){return tam;};
    //void MostraIterativo(void);
    //bool Exclui(const int &pos);
};


template <class T>
void MyList<T>::Esvazia() {
     Esvazia(primeiro);
     primeiro = ultimo = NULL;
     tam=0;
};
template <class T>
void MyList<T>::Esvazia(Cell *aux){
    if(aux==NULL) return;
    Esvazia(aux->prox);
    delete aux;
}

template <class T>
void MyList<T>::Mostra() {
    if(primeiro==NULL)
        cout << endl<<"A lista esta vazia!"<<endl;
    else
        Mostra(primeiro);
};
template <class T>
void MyList<T>::Mostra(Cell *aux){
    if(aux==NULL){
        return;
    }
    cout<<aux->val<<" ";
    Mostra(aux->prox);
}
template <class T>
bool MyList<T>::InsereNaPrimeira(const T &val){
    //se não passar a posição insere no início.
    if(primeiro==NULL) {
        primeiro = new Cell(val);
        ultimo = primeiro;
        tam++;
    } else {
        Cell *aux = new Cell(val);
        aux->prox = primeiro;
        //(*aux).prox = primeiro;
        primeiro = aux;
    }
    return true;
}
template <class T>
bool MyList<T>::InsereNaPosicao(const T &num, const int &pos){
    if(pos>tam)
        InsereNaPosicao(num,tam+1,primeiro,0);
    else
        InsereNaPosicao(num,pos,primeiro,0);

}
template <class T>
bool MyList<T>::InsereNaPosicao(const T &num, const int &pos, Cell *aux, const int &posatual) {
    if(pos-1==posatual) {
        //implementar inserção conforme desenho.
        //lembrar dos casos especiais:
        //@ inserir antes do primeiro
        //@ inserir após o último
        //nesses dois casos é necessário atualizar primeiro e ultimo (inseriu antes do primeiro ou depois do ultimo)
        return true;
    } else {
        return InsereNaPosicao(num,pos,aux->prox,posatual+1);
    }
    return false;
}

template <class T>
void MyList<T>::MostraIterativo() {
    cout << endl;
    if(tam==0){
        cout<<"\n nao tem nada na lista\n";
    }
    for(Cell *aux=primeiro; aux!=NULL;aux = aux->prox) {
        if(aux!=primeiro)
            cout << ' ';
        cout<< aux->val;
    }
    cout << endl;
}


/*
bool MyList<T>::InsereNoFim(const T &num) {
    if(tam<MAXTAM) {
        vet[tam]=num;
        tam++;
    } else {
        return false;
    }
    return true;
}
}

bool MyList<T>::Exclui(const int &pos){
    if(pos <1 || pos>(tam)) return false;
    if(tam>0) {
        for(int i=(pos); i<tam; i++) {
            vet[i-1]=vet[i];
        }
        tam--;
    }
    return true;
}
*/
char menu() {
    char c;
    cout << "\nopcoes: " <<endl;
    cout << "e: excluir" <<endl;
    cout << "i: inserir" <<endl;
    cout << "m: mostrar" << endl;
    cout << "p: insere p=0"<<endl;
    cout << "q: insere na posição desejada"<<endl;
    cout << "s: sair"<<endl;
    cout << "\nEntre com sua opcao: ";
    cin >> c;
    return c;
}

int main() {
    MyList<string> l;
    MyList<int> l2;

    l2.InsereNaPrimeira(5);
    l2.InsereNaPrimeira(1);
    l2.Mostra();
    int pos;
    string val;
    char opcao='N';
    //l.primeiro=0;
    opcao = menu();
    while(opcao!='s') {
        switch(opcao) {
        case 'e': // excluir de qualquer posicao
        case 'E':
            /*if(l.size()>0){
                do {
                    cout<< "Entre com a posicao: [1.." <<l.size()<<"]: ";
                    cin>>ws>>pos;
                } while(pos <1 || pos>(l.size()));
                l.Exclui(pos);
            } else {
                cout << "\nA lista esta vazia!";
            }*/
            break;
        case 'i':
        case 'I':
            cout<< "Entre com o numero: ";
            cin>>ws>>val;
            if(!l.InsereNaPrimeira(val))
                cout<< "Erro ao inserir, lista esta cheia!" << endl;
            break;
        case 'm':
        case 'M':
            l.Mostra();
        case 'p': // inserir na primeira posicao
        case 'P':
           /* int val;
            if(l.size()<MAXTAM){
                cout<< "Entre com o numero: ";
                cin >> ws;
                cin >> val;
                if(!l.InsereNaPrimeira(val)) {
                    cout<< "Erro ao inserir, lista esta cheia!" << endl;
                }
            } else {
                cout<< "Nao e possivel inserir pois a lista esta cheia!" << endl;
            }
            break;*/
        case 'q': // inserir qualquer posicao
        case 'Q':
            /*do {
                cout<< "Entre com a posicao: [1.." <<l.size()+1<<"]: ";
                cin>>ws>>pos;
            } while(pos <1 || pos>(l.size()+1));
            if(l.size()<MAXTAM){
                cout<< "Entre com o numero: ";
                cin >> ws;
                cin >> val;
                if(!l.InsereNaPrimeira(val,pos)) {
                    cout<< "Erro ao inserir, lista esta cheia!" << endl;
                }
            } else {
                cout<< "Nao e possivel inserir pois a lista esta cheia!" << endl;
            }*/
            break;
        default:
            cout<<"opcao invalida" << endl;
        }
        opcao=menu();
    }
    return 0;
}
