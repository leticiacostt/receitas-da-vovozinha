unit forms_main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
var
   i: Integer;
   s: String;
begin
     i:=0;
     while i<10 do begin
           i:= i+1;
           s:= s+i.ToString+', ';
     end;
     ShowMessage(s);

end;

end.

