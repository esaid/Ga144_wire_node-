<h1># Ga144_wire_node-</h1>
<p><strong>GA144  18  X  8  nodes , trouve le chemin entre un node de depart et arrivee </strong></p>
<p> exemple :   node_Depart = "402" ,  node_Arrivee = "708" </p>
<p> list_nodes_occupe = ['705', '505', '704', '608'] </p>
<p> alors le chemin sera :  </p>
<p> le node de depart :  402  </p>
<p> le node d'arrivee :  708  </p>
<p> le node : (7, 5) est occupe  </p>
<p> le node : (5, 5) est occupe  </p>
<p> le node : (7, 4) est occupe  </p>
<p> le node : (6, 8) est occupe  </p>
<p> Le chemin sera alors :  [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 7), (7, 8)]  </p>
<p> -*****************- </p>
<p> le code wire  </p>
<p> node 600 </p>
<p> east a! </p>
<p> node 708 </p>
<p> west a! </p>
<p> node 601,602,603,604,605,606 </p>
<p> wire west east </p>
<p> node 607 </p>
<p> wire west north </p>
<p> node 707 </p>
<p> wire south east </p>
<p> -*****************- </p>

<br> sur la figure1 : en rouge nodes occupes et le chemin , en bleu les nodes du chemin , en vert les nodes libres</br>

<h1># wire.py </h1>
<p> fichier qui peut etre importe depuis un autre programme python </p>
<p> exemple :   </p>
<p>from wire import wirecode, node </p>

