PGDMP     *    &        
    
    y            tabacos_ornelas    13.2    13.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    57564    tabacos_ornelas    DATABASE     l   CREATE DATABASE tabacos_ornelas WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
    DROP DATABASE tabacos_ornelas;
                postgres    false            �            1259    57565 
   inventario    TABLE       CREATE TABLE public.inventario (
    nombre_producto character varying(50) DEFAULT 'Desconocido'::character varying NOT NULL,
    precio money DEFAULT '$0.00'::money NOT NULL,
    cantidad_a_pedir integer DEFAULT 0 NOT NULL,
    cantidad_disponible integer DEFAULT 0 NOT NULL
);
    DROP TABLE public.inventario;
       public         heap    postgres    false            �            1259    57590    pedidos    TABLE     �  CREATE TABLE public.pedidos (
    numero_pedido integer NOT NULL,
    nombre_cliente character varying(60) DEFAULT 'Desconocido'::character varying NOT NULL,
    telefono_cliente character varying(10) DEFAULT 'Desconocido'::character varying NOT NULL,
    fecha_pedido date NOT NULL,
    fecha_entrega date,
    cantidad_pedido integer DEFAULT 0 NOT NULL,
    producto_pedido character varying(50) DEFAULT 'Desconocido'::character varying NOT NULL
);
    DROP TABLE public.pedidos;
       public         heap    postgres    false            �            1259    57588    pedidos_numero_pedido_seq    SEQUENCE     �   CREATE SEQUENCE public.pedidos_numero_pedido_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.pedidos_numero_pedido_seq;
       public          postgres    false    204            �           0    0    pedidos_numero_pedido_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.pedidos_numero_pedido_seq OWNED BY public.pedidos.numero_pedido;
          public          postgres    false    203            �            1259    57576    ventas    TABLE     �   CREATE TABLE public.ventas (
    numero_venta integer NOT NULL,
    cantidad_vendida integer DEFAULT 0 NOT NULL,
    fecha_venta date NOT NULL,
    producto_venta character varying(50) NOT NULL
);
    DROP TABLE public.ventas;
       public         heap    postgres    false            �            1259    57574    ventas_numero_venta_seq    SEQUENCE     �   CREATE SEQUENCE public.ventas_numero_venta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.ventas_numero_venta_seq;
       public          postgres    false    202            �           0    0    ventas_numero_venta_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.ventas_numero_venta_seq OWNED BY public.ventas.numero_venta;
          public          postgres    false    201            2           2604    57593    pedidos numero_pedido    DEFAULT     ~   ALTER TABLE ONLY public.pedidos ALTER COLUMN numero_pedido SET DEFAULT nextval('public.pedidos_numero_pedido_seq'::regclass);
 D   ALTER TABLE public.pedidos ALTER COLUMN numero_pedido DROP DEFAULT;
       public          postgres    false    203    204    204            0           2604    57579    ventas numero_venta    DEFAULT     z   ALTER TABLE ONLY public.ventas ALTER COLUMN numero_venta SET DEFAULT nextval('public.ventas_numero_venta_seq'::regclass);
 B   ALTER TABLE public.ventas ALTER COLUMN numero_venta DROP DEFAULT;
       public          postgres    false    202    201    202            �          0    57565 
   inventario 
   TABLE DATA           d   COPY public.inventario (nombre_producto, precio, cantidad_a_pedir, cantidad_disponible) FROM stdin;
    public          postgres    false    200   �       �          0    57590    pedidos 
   TABLE DATA           �   COPY public.pedidos (numero_pedido, nombre_cliente, telefono_cliente, fecha_pedido, fecha_entrega, cantidad_pedido, producto_pedido) FROM stdin;
    public          postgres    false    204   �       �          0    57576    ventas 
   TABLE DATA           ]   COPY public.ventas (numero_venta, cantidad_vendida, fecha_venta, producto_venta) FROM stdin;
    public          postgres    false    202          �           0    0    pedidos_numero_pedido_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.pedidos_numero_pedido_seq', 1, false);
          public          postgres    false    203            �           0    0    ventas_numero_venta_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.ventas_numero_venta_seq', 1, false);
          public          postgres    false    201            8           2606    57573    inventario inventario_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_pkey PRIMARY KEY (nombre_producto);
 D   ALTER TABLE ONLY public.inventario DROP CONSTRAINT inventario_pkey;
       public            postgres    false    200            <           2606    57599    pedidos pedidos_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pedidos_pkey PRIMARY KEY (numero_pedido);
 >   ALTER TABLE ONLY public.pedidos DROP CONSTRAINT pedidos_pkey;
       public            postgres    false    204            :           2606    57582    ventas ventas_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_pkey PRIMARY KEY (numero_venta);
 <   ALTER TABLE ONLY public.ventas DROP CONSTRAINT ventas_pkey;
       public            postgres    false    202            >           2606    57600    pedidos fk_producto_pedido    FK CONSTRAINT     �   ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT fk_producto_pedido FOREIGN KEY (producto_pedido) REFERENCES public.inventario(nombre_producto) ON UPDATE CASCADE;
 D   ALTER TABLE ONLY public.pedidos DROP CONSTRAINT fk_producto_pedido;
       public          postgres    false    204    2872    200            =           2606    57583    ventas fk_producto_venta    FK CONSTRAINT     �   ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT fk_producto_venta FOREIGN KEY (producto_venta) REFERENCES public.inventario(nombre_producto) ON UPDATE CASCADE;
 B   ALTER TABLE ONLY public.ventas DROP CONSTRAINT fk_producto_venta;
       public          postgres    false    202    2872    200            �      x������ � �      �      x������ � �      �      x������ � �     