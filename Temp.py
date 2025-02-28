import flet as ft

selected_value = 1 


def main(page: ft.Page):   
    page.title='Planejar contabilidade'
    page.window.width = 500
    page.window.height = 400
    page.window.resizable = False

    
    def salvar_notificaçao(e):
        page.open(ft.SnackBar(
            ft.Text('Informações salvas',color=ft.colors.WHITE),
            bgcolor=ft.colors.BLUE_400,    
            duration=2000))
        
    def botão_savequit():
        return ft.Row([   
                ft.ElevatedButton("Salvar informações", 
                                  bgcolor=ft.colors.GREEN_400,
                                  color=ft.colors.WHITE,
                                  on_click=salvar_notificaçao),
                ft.ElevatedButton("Sair", 
                                  bgcolor=ft.colors.RED_600,
                                  color=ft.colors.WHITE,
                                  on_click=lambda _:page.go('/')),],   
        alignment=ft.MainAxisAlignment.END,)
    
    
    def hvr(e):
        e.control.bgcolor = ft.colors.ORANGE_400 if e.data == "true" else ft.colors.BLUE_400
        e.control.update()

    def troca_pag(route):
        page.views.clear()     
        page.views.append(
            ft.View('/',
                    [
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text('Escolha de Beneficios',color=ft.colors.WHITE),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            center_title=True,
                            color= ft.colors.WHITE,
                            actions=[
                                ft.PopupMenuButton(
                                    bgcolor = ft.colors.BLUE,
                                    items=[
                                        ft.PopupMenuItem(text='Meu perfil',on_click=lambda _:page.go('/infopessoal')),
                                        ft.PopupMenuItem(),
                                        ft.PopupMenuItem(text='Exportar'),
                                    ]
                                )
                            ]
                        ),                                                                                                        
                        ft.Column([
                            ft.ElevatedButton("Escolher dependentes", bgcolor=ft.colors.BLUE_400,color=ft.colors.WHITE,on_click=lambda _: page.go("/dependentes"),on_hover=hvr,width=200,height=45),
                            ft.ElevatedButton("Escolher plano de saúde", bgcolor=ft.colors.BLUE_400,color=ft.colors.WHITE,on_click=lambda _: page.go("/planosaude"),on_hover=hvr,width=200,height=45),
                            ft.ElevatedButton("Escolher vale transporte", bgcolor=ft.colors.BLUE_400,color=ft.colors.WHITE,on_click=lambda _: page.go("/valetransporte"),on_hover=hvr,width=200,height=45),
                            ft.ElevatedButton("Escolher valor flash", bgcolor=ft.colors.BLUE_400,color=ft.colors.WHITE,on_click=lambda _: page.go("/flash"),on_hover=hvr,width=200,height=45),
                            ft.Container(height=15),
                            botão_savequit(),
                        ]),
                    ],
                )
            )
        
        if page.route == '/infopessoal':
            page.views.append(
                ft.View('infopessoal',
                        [    
                        ft.AppBar(
                            leading_width=40,
                            title=ft.Text('Meu perfil',color=ft.colors.WHITE),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            center_title=True,
                            color= ft.colors.WHITE),
                            ft.TextField(label="Digite seu nome", color='light_blue'),
                            ft.TextField(label="Digite sua data de nascimento", color='light_blue'),                            
                            ft.Text('Função:',size=10,theme_style=ft.TextThemeStyle.TITLE_MEDIUM,color=ft.colors.WHITE),
                            ft.CupertinoSlidingSegmentedButton(
                                selected_index=1,
                                thumb_color=ft.Colors.BLUE_400,
                                on_change=lambda e: print(f"selected_index: {e.data}"),
                                padding=ft.padding.symmetric(0, 10),
                                controls=[
                                    ft.Text("Analista"),
                                    ft.Text("Auxiliar/Assistente"),
                                    ft.Text("Gestor"),],),                            
                            ft.Text('Cargo:',size=10,theme_style=ft.TextThemeStyle.TITLE_MEDIUM,color=ft.colors.WHITE),
                            ft.CupertinoSlidingSegmentedButton(
                                selected_index=1,
                                thumb_color=ft.colors.BLUE_400,
                                on_change=lambda e: print(f"selected_index: {e.data}"),
                                padding=ft.padding.symmetric(0, 10),
                                controls=[
                                    ft.Text("Contabil"),
                                    ft.Text("Fiscal"),
                                    ft.Text("DP"),
                                    ft.Text("ADM"),
                                    ft.Text("T.i"),],),
                            botão_savequit(),
                    ]
                )
            )           

        if page.route == '/dependentes':
            page.views.append(
                ft.View('dependentes',
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Escolha de dependentes',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.ElevatedButton("Informações do primeiro dependente",bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,on_hover=hvr,on_click=lambda _: page.go("/1dependente"),width=300,height=45),                           
                            ft.ElevatedButton("Informações do segundo dependente",bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,on_hover=hvr,on_click=lambda _: page.go("/2dependente"),width=300,height=45),
                            ft.ElevatedButton("Informações do terceiro dependente", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,on_hover=hvr,on_click=lambda _: page.go("/3dependente"),width=300,height=45),
                        ]
                    )
                )
            
        if page.route == '/1dependente':
            page.views.append(
                ft.View('1dependente',                    
                        [ 
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Informação sobre o primeiro dependente',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT), 
                            ft.TextField(label="Data de nascimento",bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            ft.TextField(label="CPF",bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            ft.TextField(label="Nome", bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            botão_savequit(),
                        ]
                    )
                )
        if page.route == '/2dependente':
            page.views.append(
                ft.View('2dependente',
                        [
                           ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Informação sobre o segundo dependente',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT), 
                            ft.TextField(label="Data de nascimento",bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            ft.TextField(label="CPF",bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            ft.TextField(label="Nome", bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            botão_savequit(),   
                        ]
                    )
                )
        if page.route == '/3dependente':
            page.views.append(
                ft.View('3dependente',
                        [
                           ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Informação sobre o terceiro dependente',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT), 
                            ft.TextField(label="Data de nascimento",bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            ft.TextField(label="CPF",bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            ft.TextField(label="Nome", bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST,color=ft.colors.SURFACE_TINT),
                            botão_savequit(),   
                        ]
                    )
                )
        
        if page.route == '/planosaude':
            page.views.append(
                ft.View('planosaude',
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Escolha de Plano de saúde',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                            ft.ElevatedButton("Plano Emercor", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,on_hover=hvr,on_click=lambda _: page.go("/Emercor"),width=200,height=45),
                            ft.ElevatedButton("Plano Circulo",bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,on_hover=hvr,on_click=lambda _: page.go("/Circulo"),width=200,height=45),
                            ft.ElevatedButton("Plano Unimed", bgcolor=ft.colors.BLUE_400, color=ft.colors.WHITE,on_hover=hvr,on_click=lambda _: page.go("/Unimed"),width=200,height=45),
                        ]
                    )
                )     
        
        if page.route == '/Emercor':
            page.views.append(
                ft.View('Emercor',
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Plano Emercor',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                        ]
                    )
                ) 
        if page.route == '/Circulo':
            page.views.append(
                ft.View('Circulo',                
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Plano Circulo',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                        ]
                    )
                ) 
        if page.route == '/Unimed':
            page.views.append(
                ft.View('Unimed',
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Plano Unimed',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                        ]
                    )
                ) 
            
        if page.route == '/valetransporte':
            page.views.append(
                ft.View('valetransporte',
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Escolha do vale transporte',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text('Quantas passagens por dia você precisa?',size=20,theme_style=ft.TextThemeStyle.TITLE_MEDIUM,color=ft.colors.WHITE),],),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[

                                        ft.CupertinoSlidingSegmentedButton(
                                            selected_index=1,
                                            thumb_color=ft.colors.BLUE_400,
                                            on_change=lambda e: print(f"selected_index: {e.data}"),
                                            padding=ft.padding.symmetric(0, 10),
                                            controls=[
                                                ft.Text("1"),
                                                ft.Text("2"),
                                                ft.Text("3"),
                                                ft.Text("4"),],),],
                                ),
                            botão_savequit(),
                            ]
                        )
                    )        
        
        if page.route == '/flash':
            page.views.append(
                ft.View('flash',
                        [
                            ft.AppBar(
                                leading_width=40,
                                title=ft.Text('Escolher valor flash',color=ft.colors.WHITE),
                                center_title=True,
                                bgcolor=ft.colors.SURFACE_VARIANT),
                        ]
                    )
                ) 

        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = troca_pag
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)